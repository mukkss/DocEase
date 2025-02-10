# **DocEase 🏥 - AI-Powered Medical Chatbot**

**DocEase** is an AI-powered medical chatbot designed to provide accurate **medical information** by leveraging **DeepSeek RAG with Ollama**. It retrieves information from a **medical knowledge base** and generates responses only from verified medical sources.  

> 🚨 **Note:** This chatbot is for **informational purposes only** and does **not** replace professional medical advice.  

---

## 🌟 **Features**
✅ **Medical-Specific Knowledge Base** – Uses vector search with Pinecone for accurate retrieval.  
✅ **DeepSeek RAG + Ollama Integration** – Provides AI-generated responses based on retrieved documents.  
✅ **Strict Filtering** – Ensures only medical-related queries are answered.  
✅ **Flask API** – Easily deployable web-based chatbot.  
✅ **User-Friendly Interface** – Simple UI for interactive Q&A.  

---

## 🖼️ **Screenshots**
(Replace these placeholder images with actual ones later)  

📌 *Diseases & Conditions:*  
![Diseases & Conditions](images\Diseases & Conditions.png)  

📌 *Medical Tests & Treatments*  
![Medical Tests & Treatments](images\Medical Tests & Treatments.png)  

📌 *Preventive Medicine & Alternative Therapies:*  
![Preventive Medicine & Alternative Therapies](images\Preventive Medicine & Alternative Therapies.png)

📌 *Non Medical Example:*  
![Science & Technology](images\Science & Technology.png)  

---

## 🔧 **Installation & Setup**  

### 🚀 **Step 1: Fork the Repository**  
1. Click on the **Fork** button in the top-right of this repository.  
2. Clone your **forked version** locally:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/DocEase.git
   cd DocEase
   ```

### 🛠 **Step 2: Install Dependencies**  
Ensure you have **Python 3.8+** installed. Then, set up a virtual environment and install dependencies:  
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

### 🧠 **Step 3: Install Ollama & DeepSeek Model**  
1. Install **Ollama**:  
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh  # For Mac & Linux
   ```
   On Windows, download it from: [Ollama Website](https://ollama.ai)  

2. Pull the **DeepSeek RAG Model**:  
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

### 🏗 **Step 4: Configure Pinecone (Vector Database)**
1. Sign up at [Pinecone](https://www.pinecone.io/) and get your **API key**.  
2. Add your Pinecone API key in a `.env` file:  
   ```
   PINECONE_API_KEY=your_api_key_here
   ```

### ▶ **Step 5: Run the Application**
Start the Flask server:  
```bash
python app.py
```
The chatbot will be available at:  
📍 **http://localhost:8080**  

---

## 🎯 **Usage**
- **Enter a medical query** (e.g., *What are the symptoms of diabetes?*).  
- The chatbot **retrieves relevant documents** and generates an accurate response.  
- If the question is **not medical-related**, it will reject the query.  

---

## 📌 **Tech Stack**
- **Backend**: Flask, Python  
- **LLM**: DeepSeek RAG (via Ollama)  
- **Vector Search**: Pinecone  
- **Frontend**: HTML, CSS, JavaScript  
- **Environment**: Docker (optional)  

---

## 🚀 **Future Enhancements**
🔹 Add **speech-to-text** for voice input.  
🔹 Implement **multi-modal AI** for medical images.  
🔹 Enhance **UI with real-time chat animations**.  
🔹 Fine-tune response accuracy with **better chunking strategies**.  

---

## 🤝 **Contributing**
Want to improve **DocEase**? Fork this repo, create a feature branch, and submit a pull request!  
```bash
git checkout -b feature-branch
git commit -m "Added new feature"
git push origin feature-branch
```

---

## 📩 **Contact**
📧 Email: your.email@example.com  
🌐 GitHub: [Your Profile](https://github.com/YOUR_USERNAME)  

---

### 📌 Notes:
- **Update** the `YOUR_USERNAME` with your GitHub username.
- Replace **sample images** with real ones in the `sample_images/` folder.
- Modify the **contact details** if needed.

Now you have a well-structured **README.md**! 🎉 Let me know if you need any modifications. 🚀🔥  
