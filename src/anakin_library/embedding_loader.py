from anakin_library.config import logger
from chromadb import EmbeddingFunction, Embeddings, Documents
from sentence_transformers import SentenceTransformer
import os

class EmbeddingLoader(EmbeddingFunction):
    def __init__(self, embedding_model, model_dir):
        """
        Initializes the EmbeddingLoader class based on the model loading mode.
        """
        self.embeddings = []
        logger.info("Loading {} model".format(embedding_model))
        if model_dir:
            self.local_model = SentenceTransformer(model_name_or_path=os.path.join(model_dir, embedding_model))
        else:
            self.local_model = SentenceTransformer(embedding_model)
        logger.info("Model has been loaded successfully!")

    def __call__(self, input_text: Documents, context: str) -> Embeddings:
        """
        Generates embeddings for the input_text based on a local model inference or an API call.

        :param input_text: input document text for the embedding generation
        :param context: addresses context to the input text
        :return: embedded representation of the input document text based on the local model or the API call.
        """
        if context:
            input_text = context + " " + input_text
        return self.local_model.encode(input_text).tolist()
