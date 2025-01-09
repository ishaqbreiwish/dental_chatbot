# Dental Chatbot

## Overview

The Dental Chatbot is an AI-powered assistant designed to provide users with information and support related to dental health. It utilizes advanced natural language processing techniques to understand user queries and provide relevant responses based on a collection of pre-embedded documents.

## Features

- **Contextual Responses**: The chatbot generates responses based on the context provided by relevant documents.
- **Integration with Hugging Face**: Utilizes Hugging Face's API for embedding documents and queries.
- **ChromaDB for Storage**: Stores and retrieves embeddings efficiently using ChromaDB.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dental_chatbot.git
   cd dental_chatbot
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add your Hugging Face token and OpenAI API key:
     ```
     HF_TOKEN=your_hugging_face_token
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

To run the chatbot, execute the following command:
`python dental_chatbot/backend/main.py`
