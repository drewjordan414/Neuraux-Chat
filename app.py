# Import libraries
import os
import openai
import gradio as gr

# Load sensitive information from a configuration file
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Set up the OpenAI API key
openai.api_key = config['openai']['api_key']

# Define sequence variables
s_sequence = "\nBot:"
r_sequence = "\nHuman: "

prompt = []

def generate_response(prompt, temperature):
    """Function to create a response
    Args:
        prompt (str): piece of text or a set of instructions that is provided as input
        temperature (float): the sampling temperature for the response generation
    Returns:
        str: text
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " Bot:"],
        )
        return response.choices[0].text
    except Exception as e:
        print("Error:", e)
        return "An error occurred while generating a response."

def clone(input, history, temperature):
    """Function to build Gradio Application
    Args:
        input (str): text from user
        history (str): stores the state of the current gradio application
                      | stores knowledge of context of memory what is happening in past as well
        temperature (float): the sampling temperature for the response generation
    Returns:
        tuple: output and state
    """
    try:
        history = history or []
        s = list(sum(history, ()))
        s.append(input)
        inp = " ".join(s)
        output = generate_response(inp, temperature)
        history.append((input, output))
        return history, history
    except Exception as e:
        print("Error:", e)
        return "An error occurred while processing the input.", history


# Build web applications that combine markdown, HTML, buttons, and interactive components
block = gr.Blocks()

with block:
    gr.Markdown(
        """<h1><center>Neurax-Chat</center></h1>
    """
    )
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")

    # Add temperature slider
    temperature_slider = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, default=0.9, label="Temperature")

    # Update submit.click() to include the temperature_slider
    submit.click(clone, inputs=[message, state, temperature_slider], outputs=[chatbot, state])

block.launch(debug=True)


