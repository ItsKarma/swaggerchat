__import__('pysqlite3')
import os
import sys

from langchain.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

KEY = os.getenv('OPENAI_API_KEY')
ORG_ID = os.getenv('OPENAI_ORG_ID')
EXPORTED_DIR = "./exported"

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


query = sys.argv[1]

txt_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.txt", show_progress=True, loader_cls=TextLoader)
json_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.json", show_progress=True, loader_cls=TextLoader)
csv_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.csv", show_progress=True, loader_cls=TextLoader)
xml_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.xml", show_progress=True, loader_cls=TextLoader)
python_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.py", show_progress=True, loader_cls=TextLoader)
javascript_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.js", show_progress=True, loader_cls=TextLoader)
terraform_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.tf", show_progress=True, loader_cls=TextLoader)
pdf_loader = DirectoryLoader(
    EXPORTED_DIR, glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)


index = VectorstoreIndexCreator().from_loaders(
    [txt_loader, json_loader, csv_loader, xml_loader, python_loader, javascript_loader, terraform_loader, pdf_loader])

print() # Just creating a blank line for readability
print(index.query(query, llm=ChatOpenAI(openai_organization=ORG_ID, openai_api_key=KEY)))
