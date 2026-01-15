# Gen_AI_examples
Systems that derives inspiration from the provided content and uses it to create something new, can be categorized as Generative AI.  There are many models from various providers used to achieve this.

## 1. Image label generation
After capturing thousands of images of the past 20 years it can be difficult to track down or retieve the ones you want.  There is commercial software available, such as Eagle, for annotations an labels.  However you would still have to review the images and design a tagging or labeling nomenclature stategy. 
Computer Visin Systems that can generate natural language descriptions of images.

This example project captures 3 different approaches.
1. Python Scripting  
2. Hugging Face supplied models to label the image activity 
3. Vector Database & Index methods to capture activity (precursor for RAG)

## 2. Summarizing Private Data
Created a Chatbot as a Python Flask app that can examine your private data and summarize the information.  This Langchain based app, embeds your private data using Chroma (VectorDB) and generates the appropriate prompts for using an LLM, meta-llama.  The model was obtained using WatsonX and the transformer using HuggingFace.

It is a Flask application consisting of a Server and Worker components.  

## 3. AI Meeting Assistant
AI-Powered Meeting Assistant project offers a modern, transformative solution for meeting documentation. By leveraging large language models (LLMs) and generative AI, this project equips participants with the tools to automate note-taking and extract critical insights efficiently.

Using advanced natural language processing, generative AI identifies and captures key meeting elements in real-time, including ideas, decisions, action items, and deadlines. This eliminates the need for manual note-taking, allowing team members to focus fully on the conversation without worrying about missing important details. The AI not only transcribes discussions but also organizes the content into clear, structured, and actionable meeting minutes. These organized records serve as a reliable resource that enhances clarity, improves follow-ups, and ensures teams stay aligned and productive as they move forward confidently.

Update the API Key and Project ID for usage 