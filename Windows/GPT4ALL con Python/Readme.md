## GTP4ALL con Python

### Maquina utilizada:

### Componentes y SW: 

### <ul><li>Modelo: TUF GAMING FX505DY</li><li>Sistema Operativo: Windows 11</li><li>Procesador: Ryzen 5 3550H</li><li>Almacenamiento: SSD 250GB, HDD 1TB</li><li>RAM: 16GB</li></ul>

### Uso de Python con libreria GPT4all (Utilizando Windows)

### <li>En mi caso utilizare Jupyter Notebook el cual es parte de Anaconda</li>

### <li>Para usar la libreria de GTP4ALL debemos de instalar la libreria, con el comando <code>pip install gpt4all</code> ejecutandolo desde una consola de comandos que reconozca pip</li>

![Python_2](https://github.com/RETBOT/ChatDynamix/assets/71898783/e8063aba-3bfa-40e3-8481-2e3fbbfe09f7)

### <li>Para finalizar debemos de ejecutar el import de la libreria gtp4all y realizar la petion en la parte de "content"</li>

![Python](https://github.com/RETBOT/ChatDynamix/assets/71898783/506bcd6e-68c3-47a4-905c-0a4b37d968ea)

### Nota: La cantidad de tiempo que tome la ejecucion dependera de tu maquina, esto debido a que corre de manera local.

## Servidor con GPT4ALL Chat UI

### <li>Para hacer uso de GTP4ALL a modo de servidor para realizar peticiones, debemos de abrir GTP4ALL y habilitar el modo de <b>Enable Web Server</b>. Como se ve a continuacion:</li>

### <li>Una vez que habilitemos la opcion, podemos posicionarnos en el menu de la izquierda en la parte de Server Chat para poder monitorear las peticiones que se realicen en el server.</li>

### <li>Ahora para realizar peticiones en mi caso hare uso de Python para realizar la peticion. Debemos de instalar la libreria de openai, con el siguiente comando desde una terminal con el pip habilitado <code>pip install openai</code>.</li>

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



