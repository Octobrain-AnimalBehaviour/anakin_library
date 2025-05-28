from typing import List, Tuple
from chromadb import Client, PersistentClient
from chromadb.utils import embedding_functions
from tqdm import tqdm
from ..common.config import logger
from ..embedding.embedding_loader import EmbeddingLoader

class VectorDBClient:
    def __init__(self, db_dir, top_k_elements, embedding_loader: EmbeddingLoader):
        self.__db_path = db_dir
        self.__top_k = top_k_elements
        if embedding_loader is None:
            self.__embedding_model = embedding_functions.DefaultEmbeddingFunction()
        self.__embedding_model = embedding_loader

    def __call__(self, query: str, db_name: str, documents: List) -> List:
        """
        Creates or Loads the db instance to extract relevant passages based on the query.

        :param query: question of interest
        :param db_name: name of the db collection instance
        :param documents: list of all the identified chunks from the documents.
        :return: list of relevant passages based on the query.
        """
        self.chroma_client = PersistentClient(path=self.__db_path)
        self.db = self.__create_or_load(db_name, documents)

        passages = self.__get_relevant_passages(query)
        return passages

    def __create_or_load(self, db_name: str, documents: List) -> Client:
        """
        Loads the db instance, if the name is found in the list of collections.
        Creates a new one, otherwise.

        :param db_name: name of the db collection instance.
        :param documents: list of all the identified chunks from the documents.
        :return: db collection instance
        """
        if db_name in [c.name for c in self.chroma_client.list_collections()]:
            logger.info("DB already exists, Loading...")
            return self.__load_chroma_db(db_name, documents)
        else:
            return self.__create_chroma_db(db_name, documents)

    def __load_chroma_db(self, db_name: str, documents: List):
        """
        Loads the db instance based on the db_name and aggregates the documents that are not part of the collection.

        :param db_name: name of the db collection instance.
        :param documents:list of all the identified chunks from the documents.
        :return:db collection instance
        """
        db = self.chroma_client.get_collection(name=db_name, embedding_function=self.__embedding_model)
        all_metadata = db.get(include=["metadatas"]).get('metadatas')
        distinct_files = set([x.get('file_name') for x in all_metadata])
        max_id = db.count() + 1

        count_new_files = 0
        for i, d in enumerate(tqdm(documents)):
            if d[1] not in distinct_files:
                db.add(documents=[d[0]], ids=[str(max_id + i)], metadatas=[{"file_name": d[1]}])
                count_new_files += 1
        logger.info("New chunks added: {}".format(count_new_files))
        return db


    def __create_chroma_db(self, db_name: str, documents: List) -> Client:
        """
        Creates the db instance based on the db_name and aggregates all the documents of the list.

        :param db_name: name of the db collection instance.
        :param documents: list of all the identified chunks from the documents.
        :return: db collection instance
        """
        db = self.chroma_client.create_collection(name=db_name, embedding_function=self.__embedding_model)

        logger.info("Embedding creation process has started...")
        for i, d in enumerate(tqdm(documents)):
            db.add(documents=[d[0]], ids=[str(i)], metadatas=[{"file_name": d[1]}])
        return db

    def __get_relevant_passages(self, query: str) -> List:
        """
        Extracts the top-k most relevant passages from the collection based on the input query.
        The query is performed using the cosine similarity.

        :param query: question of interest
        :return: a list of the top_k most relevant passages for the input query.
        """
        passages = self.db.query(query_texts=[query], n_results=self.__top_k, include=['distances', 'documents'])
        passages = [{"id": str(i), "snippet": str(text)} for i, text in zip(passages.get("ids")[0], passages.get("documents")[0])]
        return passages

    def return_passage(self, id: int) -> Tuple[str, str]:
        """
        Retrieves the text and the name of the document based on the id.

        :param id: identification number of the passage needed.
        :return: the text of the passage and the name of the document from where it was extracted.
        """
        register = self.db.get(ids=[str(id)], include=['documents', 'metadatas'])
        passage = register.get("documents")[0] if register.get("documents") else "Passage not found"
        document_name = register.get("metadatas")[0].get("file_name", "File not found") if register.get("metadatas") else "File not found"
        return passage, document_name
