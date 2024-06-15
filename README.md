# RAG with Youtube videos

This project leverages LangChain, OpenAI, ChromaDB, and Gradio to create a question-answering system for any YouTube videos. By inputting questions related to the content of the provided videos, users receive answers along with a corresponding YouTube video.

## Features

- Extracts and translates text from YouTube videos.
- Splits text into manageable chunks for processing.
- Embeds text data using OpenAI embeddings.
- Stores and retrieves text data efficiently using Chroma vector store.
- Generates answers to questions using OpenAI's language model.
- Displays both the answer and the related YouTube video in an interactive Gradio interface.

## Setup

### Prerequisites

- OpenAI API key
- Necessary Python packages (specified in the `requirements.txt`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MuratcanLaloglu/openai-rag-with-youtube-transcripts-and-chromadb-ai-assistant.git
   
   cd openai-rag-with-youtube-transcripts-and-chromadb-ai-assistant
2. **Install the required packages:**

    ```
    pip install -r requirements.txt
    ```
3. **Set your OpenAI API key:**
Replace "put your openai api key here" in the code with your actual OpenAI API key.

4. **Add YouTube URLs:**
Replace "put your youtube video links here" with the URLs of the YouTube videos you want to process.


## Usage

1. **Run the notebook**

2. **Open your web browser and go to the URL provided by Gradio**

### Interacting with the Interface

- **Ask a question:** Type your question related to a video in the input box.

- **View the answer and video:** The system will display the answer and embed the related YouTube video.







