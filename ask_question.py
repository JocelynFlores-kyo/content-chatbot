import argparse
import faiss
import os
import pickle

from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain

parser = argparse.ArgumentParser(description='Paepper.com Q&A')
parser.add_argument('question', type=str, help='Your question for Paepper.com')
args = parser.parse_args()

# with open("faiss_store.pkl", "rb") as f:
#     store = pickle.load(f)

# 修改加载方式
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

store = FAISS.load_local(
    "faiss_store",  # 目录路径（无需后缀）
    OpenAIEmbeddings(), 
    allow_dangerous_deserialization=True  # 允许加载旧版序列化数据
)

chain = VectorDBQAWithSourcesChain.from_llm(
        llm=OpenAI(temperature=0, verbose=True), vectorstore=store, verbose=True)
result = chain({"question": args.question})

print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
