from flask import Flask, request
import gpt4all

app = Flask(__name__)

# Global variable to store the initial prompt
prompt = "Hi"

# Global variable to store the library, loaded at startup
lib = "ggml-gpt4all-j-v1.3-groovy"
# After installing the library, uncomment this line to make the conversations faster.
# gptj = gpt4all.GPT4All(lib)

# Route to display the current prompt
@app.route('/')
def index():
   # Displays the current prompt.
   return prompt

# Route to install the library
@app.route('/install')
def install():
   # Installs the library
   global lib

   gptj = gpt4all.GPT4All(lib)
   return 'Library installed: '+lib


# Route to install a new library
@app.route('/install', methods=['POST'])
def install_post():
   # Installs a new library specified in the request form.
   global lib
   global gptj

   lib = request.form['lib']
   gptj = gpt4all.GPT4All(lib)
   return 'Library installed: ' + lib

# Route to receive a value via HTTP and update the prompt
@app.route('/update-prompt', methods=['POST'])
def update_prompt():
   # Updates the prompt with the value specified in the request form.
   global prompt
   prompt = request.form['value']
   return 'Prompt updated: ' + prompt

# Route to generate a response using the updated prompt
@app.route('/chat', methods=['POST'])
def generate_response():
   # Generates a response using the updated prompt.
   global prompt
   global gptj

   prompt = request.form['value']
   messages = [{"role": "assistant", "content": "As an experienced AI assistant, I'll help you with programming questions and provide code solutions in your preferred language. Your name is ChatDynamix"}, {"role": "user", "content": prompt}]
   response = gptj.chat_completion(messages)
   return response

if __name__ == '__main__':
   app.run()