# Neurax-Chat
# Comp150-Final
 Neurax-Chat is a chatbot application powered by OpenAI's GPT-3 model. It provides a simple web-based interface that allows users to interact with the AI model in a conversational manner. This porject was built around OpenAI's API and as a final project for the COMP150 at Loyola University Chicago

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Function Descriptions](#function-descriptions)

## Installation

To set up the application, you'll need to install the required libraries:

```bash
pip install openai gradio

You'll also need to create a config.ini file containing your OpenAI API key:
    [openai]
    api_key=your_api_key_here

Make sure to replace your_api_key_here with your actual API key.

# FOR THE API KEY
- You will need to navigate to this link https://platform.openai.com/account/api-keys
- Once you click on that link, you will need to sign in or create an account with OpenAI
- From there click on "Create New Key" 
  - Note that once you create your key it will show your key only ONCE
  - Save your key in a safe place!

## Usage
To run the application, simply execute the script:
python app.py
This will launch a Gradio web application in your browser where you can interact with the chatbot.

## Function Discriptions
- generate_response(prompt, temperature): Generates a response based on the input prompt and temperature.
- prompt: A piece of text or a set of instructions that is provided as input.
- temperature: The sampling temperature for the response generation.
- clone(input, history, temperature): Builds the Gradio application.
- input: Text input from the user.
- history: Stores the state of the current Gradio application and keeps track of past interactions.
- temperature: The sampling temperature for the response generation.
