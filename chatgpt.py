import os
import sys

from langchain.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

KEY = os.getenv('OPENAI_API_KEY')

query = sys.argv[1]
print(query)

txt_loader = DirectoryLoader(
    "./exported", glob="**/*.txt", show_progress=True, loader_cls=TextLoader)
json_loader = DirectoryLoader(
    "./exported", glob="**/*.json", show_progress=True, loader_cls=TextLoader)
csv_loader = DirectoryLoader(
    "./exported", glob="**/*.csv", show_progress=True, loader_cls=TextLoader)
xml_loader = DirectoryLoader(
    "./exported", glob="**/*.xml", show_progress=True, loader_cls=TextLoader)
pdf_loader = DirectoryLoader(
    "./exported", glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)


index = VectorstoreIndexCreator().from_loaders(
    [txt_loader, json_loader, csv_loader, xml_loader, pdf_loader])

print(index.query(query, llm=ChatOpenAI()))
