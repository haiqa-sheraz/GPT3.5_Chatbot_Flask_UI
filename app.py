from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role":"user", "content":prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    if 'choices' in response and response['choices']:
        content = response['choices'][0]['message']['content']
        return content
    else:
        return None

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = get_completion(userText)
    
    print("User Input:", userText)
    print("Chatbot Response:", response)
    
    if response:
        return response
    else:
        return "No response from the chatbot"

if __name__ == "__main__":
    app.run()
    
    