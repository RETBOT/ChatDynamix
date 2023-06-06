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




