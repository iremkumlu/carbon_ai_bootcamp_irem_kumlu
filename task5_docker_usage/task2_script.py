from fastapi import FastAPI
from pydantic import BaseModel
import os
from haystack.document_stores import FAISSDocumentStore
from haystack import Document
from haystack.nodes import PreProcessor, EmbeddingRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline


# FastAPI Uygulaması
app = FastAPI()

# Veritabanı ve işlem hazırlığı
document_store = FAISSDocumentStore(sql_url="sqlite:///", faiss_index_factory_str="Flat")
file_names = [os.path.join('Data', 'doc1.txt'), os.path.join('Data', 'doc2.txt'), os.path.join('Data', 'doc3.txt')]
documents = [Document(content=open(file, 'r', encoding='utf-8').read()) for file in file_names]

# Veri Önişleme
preprocessor = PreProcessor(clean_empty_lines=True, clean_whitespace=True, split_by="word", split_length=100)
processed_docs = preprocessor.process(documents)
document_store.write_documents(processed_docs)

retriever = EmbeddingRetriever(document_store=document_store, embedding_model="savasy/bert-base-turkish-squad")
document_store.update_embeddings(retriever)

reader = FARMReader(model_name_or_path="savasy/bert-base-turkish-squad", use_gpu=True)
pipe = ExtractiveQAPipeline(reader, retriever)

# Veri modeli
class QueryModel(BaseModel):
    query: str

@app.post("/chat/")
async def chat(query_model: QueryModel):
    query = query_model.query
    prediction = pipe.run(query=query, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 1}})
    
    cevaplar = ""
    for answer in prediction['answers']:
        cevaplar += f"{answer.answer} {answer.context}\n\n"
        
    if cevaplar:
        return {"answers": cevaplar}
    else:
        return {"answers": "Bu konuda bir cevap bulunamadı."}

