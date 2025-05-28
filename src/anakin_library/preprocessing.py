import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from anakin_library.config import PDF,logger
from langchain_community.document_loaders import PyPDFLoader as pdf


def load_pdf(file_path: str) -> List:
    """
    Extracts text and generate chunks from the pdf document

    :param file_path: path of the pdf file
    :return: identified chunks from the pdf file
    """
    texts = []
    loader = pdf(file_path)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200,
                                                   separators=["\n\n", "\n", " ", ".", ","])
    pages = loader.load_and_split(text_splitter)
    for p in pages:
        texts.append(p.page_content)
    return texts


def load_files(data_dir: str) -> List:
    """
    Extracts the text from the files identified in the data_dir according to the document type.
    Returns a list of the identified chunks.

    :param data_dir: directory of the data files for the chunks extraction.
    :return: list of the identified chunks.
    """
    passages = []
    pdf_count = 0

    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)
        file_name = os.path.basename(filename)
        file_type = file_name.split('.')[-1].lower()

        texts = ""
        if file_type == PDF:
            texts = [[txt, file_name] for txt in load_pdf(file_path)]
            pdf_count += 1
        else:
            texts = None
            logger.info("This is not a pdf, passed:", file_name)
            pdf_count += 1

        if texts:
            if isinstance(texts, list):
                passages.extend(texts)
            else:
                passages.append(texts)

    logger.info("Number of files processed: {}".format(pdf_count))
    logger.info("Total number of passages extracted: {}".format(len(passages)))
    return passages
