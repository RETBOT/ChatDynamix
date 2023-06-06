# Instalacion de GTP4ALL en Windows

### Maquina utilizada:

### <ul><li>Modelo: TUF GAMING FX505DY</li><li>Sistema Operativo: Windows 11</li><li>Procesador: Ryzen 5 3550H</li><li>Almacenamiento: SSD 250GB, HDD 1TB</li><li>RAM: 16GB</li></ul>

### Instalacion de GTP4ALL en Windows (Disponible para cualquier version de Windows)

### <li>Debemos ingresar al sitio oficial de gpt4all (<a href="https://gpt4all.io/index.html">Enlace</a>). Debemos de clickear el boton de <b>Windows Installer</b></li>

![Paso_1](https://github.com/RETBOT/ChatDynamix/assets/71898783/57c67017-aeb6-4b9f-9b80-035620fe1208)

### <li>Debemos de buscar el archivo .EXE descargado en la carpeta de Descargar o Downloads. Al encontrarlo debemos de ejecutarlo como Administrador</li>

![Paso_2](https://github.com/RETBOT/ChatDynamix/assets/71898783/17cf57a0-0172-4b3a-abd2-9c9aee356306)

### <li>La instalacion es sencilla, a todas pantallas damos click en "Siguente". La parte importante es la descarga de los archivos, como se ve a continuacion:</li>

![Paso_4](https://github.com/RETBOT/ChatDynamix/assets/71898783/70f73efa-9719-45c8-9f87-1fee5cac55ff)

### <li>Para abrir el archivo debemos de buscarlo como cualquier otro programa, como se ve a continuacion: </li>

![GTP](https://github.com/RETBOT/ChatDynamix/assets/71898783/e3f508e4-3e0c-47d0-8f2f-91b279f9ed22)

### <li>Al abrirlo por primera vez debemos de descargar algun modelo de lenguaje generativo y debemos de esperar a terminar la descarga. Un modelo GPT4All es un archivo de 3 GB a 8 GB que puede descargar y conectar al software del ecosistema de código abierto GPT4All. </li>

![Paso_7](https://github.com/RETBOT/ChatDynamix/assets/71898783/4f647ce5-78b1-4cb7-a9e3-d923708d8d5b)

### <li>Al final podremos realizar peticiones al modelo seleccionado, sin necesidad de utilizar ancho de banda en las peticiones y 100% de manera local.</li>

![Final](https://github.com/RETBOT/ChatDynamix/assets/71898783/556257d3-939d-48de-9b67-c807decd667e)

## Servidor con GPT4ALL Chat UI

### <li>Para hacer uso de GTP4ALL a modo de servidor para realizar peticiones, debemos de abrir GTP4ALL y habilitar el modo de <b>Enable Web Server</b>. Como se ve a continuacion:</li>

![enable_web_server](https://github.com/RETBOT/ChatDynamix/assets/71898783/5c6399d1-33d1-405c-925a-04613b97b693)

### <li>Una vez que habilitemos la opcion, podemos posicionarnos en el menu de la izquierda en la parte de Server Chat para poder monitorear las peticiones que se realicen en el server.</li>

![logs](https://github.com/RETBOT/ChatDynamix/assets/71898783/a623d017-1d7a-4899-9ad5-839430523019)

### <li>Ahora para realizar peticiones en mi caso hare uso de Python para realizar la peticion. Debemos de instalar la libreria de openai y para esto debemos de abrir en mi caso al usar Anaconda abriré Anaconda PowerShell Prompt</li>

![anaconda](https://github.com/RETBOT/ChatDynamix/assets/71898783/a59cffed-2ba9-43f2-acde-e16407657082)

### <li>Para instalar la libreria necesaria debemos usar el siguiente comando <code>pip install openai</code>.</li>

![librerias](https://github.com/RETBOT/ChatDynamix/assets/71898783/32fdd638-2f3a-4ca3-af4a-68c2218ed4f6)

### <li>Una vez que la instalacion finalice, podemos hacer uso del codigo que comparte la documentacion de GTP4ALL, el cual es:</li>

    ```Python
    import openai
    openai.api_base = "http://localhost:4891/v1"
    #openai.api_base = "https://api.openai.com/v1"

    openai.api_key = "not needed for a local LLM"

    # Set up the prompt and other parameters for the API request
    prompt = "Te gustan las galletas?"

    # model = "gpt-3.5-turbo"
    #model = "mpt-7b-chat"
    model = "gpt4all-j-v1.3-groovy"

    # Make the API request
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=50,
        temperature=0.28,
        top_p=0.95,
        n=1,
        echo=True,
        stream=False
    )

    # Print the generated completion
    print(response)
    ```

### <li>Con la peticion antes realizada ("Te gustan las galletas") nos debe de aparecer lo siguiente tanto en el editor donde se ejecute la peticion al igual que en el GTP4ALL en la parte de Server Chat</li>

![galletas](https://github.com/RETBOT/ChatDynamix/assets/71898783/24099897-0287-4e57-8dd5-16ac9132b574)

![mas_galletas](https://github.com/RETBOT/ChatDynamix/assets/71898783/27d471d6-da10-44c2-a4aa-2fd4b39043b4)

## Servidor de GPT4ALL con Python (Para peticiones con terceros)

### Para poder hacer un servidor de este tipo se debe de tener un archivo .py el cual este corriendo en terminal para poder realizar peticiones en tiempo real.

### <li>Para ello en mi caso al usar Anaconda podemos ejecutar la <b>Anaconda PowerShell Prompt<b> en la cual ejecutaremos el archivo .py</li>
    
![anaconda](https://github.com/RETBOT/ChatDynamix/assets/71898783/511bfcd4-9797-4912-823d-53b1b811a8a1)

### <li>El servidor ejecutará codigo tanto de tipo POST como GET para las peticiones, el codigo es el siguiente:</li>
```Python
    from flask import Flask, request
    import gpt4all

    app = Flask(__name__)

    # Global variable to store the initial prompt
    prompt = "Hi"

    # Global variable to store the library, loaded at startup
    lib = "ggml-gpt4all-j-v1.3-groovy"
    gptj = gpt4all.GPT4All(lib)

    # Route to display the current prompt
    @app.route('/')
    def index():
        # Displays the current prompt.
        return prompt

    # Route to install the library
    @app.route('/install')
    def install():
        # Installs the library ggml-gpt4all-j-v1.3-groovy.
        global gptj
        gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")
        return 'Library installed: ggml-gpt4all-j-v1.3-groovy'


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
```
### <li>Para ejeuctar debemos de utilizar el comando <code>python servidor.py</code>, el cual nos mostrará lo siguiente:</li>
![Server2](https://github.com/RETBOT/ChatDynamix/assets/71898783/bbc1c3cf-82b4-4746-9eee-f942246ad382)

### <li>Al final para realizar en mi caso utilizaré Postman en el cual realizare una peticion POST, enviando un valor que sera "¿Cual es tu nombre maquina?" y nos debe mostrar:</li>
![Postman-chat](https://github.com/RETBOT/ChatDynamix/assets/71898783/189f967e-bf34-4dc4-a446-bc269c26a979)


