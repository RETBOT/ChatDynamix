from flask import Flask, request
import gpt4all

app = Flask(__name__)

# Global variable to store the initial prompt
prompt = "Hi"

# Global variable to store the library
lib = "ggml-gpt4all-j-v1.3-groovy"

# Main route to display the current prompt
@app.route('/')
def index():
    return prompt

# Route to install the library
@app.route('/install')
def install():
    gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")
    return 'Library installed: ggml-gpt4all-j-v1.3-groovy'

# Route to install the library via POST request
@app.route('/install', methods=['POST'])
def install_post():
    global lib

    lib = request.form['lib']
    gptj = gpt4all.GPT4All(lib)
    return 'Library installed: ' + lib

# Route to receive the value via HTTP and update the prompt
@app.route('/update-prompt', methods=['POST'])
def update_prompt():
    global prompt
    prompt = request.form['value']
    return 'Prompt updated: ' + prompt

# Route to generate the response using the updated prompt
@app.route('/chat', methods=['POST'])
def generate_response():
    global prompt
    global lib

    prompt = request.form['value']
    gptj = gpt4all.GPT4All(lib)
    messages = [{"role": "user", "content": prompt}]
    return str(gptj.chat_completion(messages))

if __name__ == '__main__':
    app.run()
