# ollama_excersies
This repository contains examples of interacting with the Llama2 model using Ollama's API. It includes a Jupyter notebook with examples and a Streamlit app for live interaction with the model.

Getting Started
Prerequisites
To run the code in this repository, you will need:

* Python 3.10 or higher
* Ollama API client
* Jupyter Notebook or any compatible editor for .ipynb files
* Streamlit for running the Streamlit app
Installation
Clone the repository:
* git clone https://github.com/your-username/ollama-examples.git cd ollama-examples

Install the required packages:  
* pip install ollama streamlit

# Notebook Overview
The provided notebook (ollama_examples.ipynb) contains a series of examples demonstrating the following:
* Every cell shows the code of an ollama example.
* Model Setup: How to initialize and interact with the Llama2 model using Ollama's Python API.
* Handling Model Responses: Capture and print responses from the model, including specific tool calls (e.g., fetching flight times).
* Asynchronous Calls: Use of asyncio to handle asynchronous API interactions with the model.
Note: The last four cells in the notebook are not currently functional. They are included as placeholders for further exploration or development.

# Streamlit App (ollstr.py)
Additionally, this repository contains a Streamlit app (ollstr.py) that provides a simple UI for interacting with the Llama2 model.

* The user enters a prompt into the chat box.
* The prompt is sent to the Llama2 model using the Ollama API.
* The model's response is streamed back to the user word by word, simulating a live conversation.
# Running the Streamlit App    
To start the Streamlit app, run the following command in your terminal:

streamlit run ollstr.py
