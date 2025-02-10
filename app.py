from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medicalbot"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.8, "k": 3}  # Increase threshold if needed
)

# Initialize the DeepSeek model from Ollama
llm = Ollama(model="deepseek-r1:1.5b", temperature=0.4, num_predict=750)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')


def strict_medical_rag(query):
    retrieved_docs = retriever.invoke(query)  # Step 1: Retrieve documents
    print("\n🔎 Retrieved Documents:\n", retrieved_docs)  # Debugging step
    
    # Step 2: If no relevant medical docs found, return strict response
    if not retrieved_docs:
        return {"answer": "I'm sorry, but I can only answer medical-related questions."}
    
    # Step 3: Otherwise, pass query and context to RAG chain
    response = rag_chain.invoke({"input": query, "context": retrieved_docs})
    return {"answer": response["answer"]}


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form.get("msg")  # Get user input safely
    print(f"User Input: {msg}")

    # Step 1: Process query through strict RAG function
    response = strict_medical_rag(msg)
    
    # Step 2: Clean unwanted tags (if necessary)
    cleaned_answer = response["answer"].split("</think>")[-1].strip()
    print("Response : ", cleaned_answer)
    return str(cleaned_answer)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

