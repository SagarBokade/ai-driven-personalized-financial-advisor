from flask import Flask, request, jsonify, render_template
from huggingface_hub import InferenceClient
import json
from datetime import datetime

app = Flask(__name__)

# Specify the model repository ID and initialize the Hugging Face client
repo_id = "microsoft/Phi-3.5-mini-instruct"
llm_client = InferenceClient(model=repo_id, timeout=120, token='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')  # Replace with your actual token

# Greeting logic based on the time of day
def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

@app.route('/')
def index():
    # Render the chat interface HTML file
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("input")
    print(f"Received input: {user_input}")  # Debug log for received input

    # Handle greeting for the first interaction
    if user_input.lower() in ["hi", "hii", "hello", "hey"]:
        greeting = get_greeting()
        return jsonify({"response": f"{greeting}, I am an AI-driven financial advisor. You can ask any finance-related questions! How can I help you today?"})

    # Define a structured financial advice prompt
    prompt = f"You are a financial advisor AI. Provide relevant financial advice concisely based on the following input: {user_input}"

    try:
        # Call the Hugging Face model with the user input
        response = llm_client.post(
            json={
                "inputs": prompt,
                "parameters": {"max_new_tokens": 500},
                "task": "text-generation",
            },
        )
        
        # Parse and decode the response
        generated_response = json.loads(response)
        
        # Extract the generated text
        bot_reply = generated_response[0]["generated_text"].strip()

        # Clean up the response to remove any instructions or prompt remnants
        if "Provide relevant financial advice concisely based on the following input:" in bot_reply:
            bot_reply = bot_reply.split("Provide relevant financial advice concisely based on the following input:")[-1].strip()
        
        # Further clean the response in case of multiple instructions or repetitions
        bot_reply = bot_reply.replace("You are a financial advisor AI.", "").strip()

        return jsonify({"response": bot_reply})
    
    except Exception as e:
        # Handle any exceptions during response generation
        return jsonify({"response": f"Sorry, I could not generate a response: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)

