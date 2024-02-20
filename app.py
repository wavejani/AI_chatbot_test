# Importing modules
from transformers import pipeline
import gradio as gr

# Loading the pretrained chatbot model from Hugging Face Transformers
chatbot = pipeline(model="facebook/blenderbot-400M-distill")
                   
message_list = []
response_list = []

# Function to generate text based on the provided prompt
def cool_chatbot(message, history):
    # Add the current message to the message history
    message_list.append(message)
    # Use the chatbot to generate a response
    response = chatbot(message)[0]['generated_text']
    # Add the generated response to the response history
    response_list.append(response)
    # Return the generated response
    return response

# Launching the Gradio interface for text generation
demo_chatbot = gr.ChatInterface(cool_chatbot, title="Cool Chatbot", description="Enter text to start chatting.")

demo_chatbot.launch()








