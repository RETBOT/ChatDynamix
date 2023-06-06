# Instalación de gpt4all para Linux Ubuntu

En este documento se describe cómo instalar y configurar gpt4all en Linux Ubuntu. También se proporcionan ejemplos de código para realizar solicitudes utilizando la interfaz de chat GPT4All Chat UI y la API de Python de GPT4All.


![img-postman](./imgs/Name.png)

## Instalación

Sigue estos pasos para instalar gpt4all en Ubuntu:

1. Abre tu navegador web y visita la página oficial de [GPT4ALL](https://gpt4all.io/index.html).
   ![img-1](./imgs/1.png)

2. Descarga el instalador para Ubuntu desde la página web.
   ![img-2](./imgs/2.png)

3. Una vez finalizada la descarga, tendrás un archivo llamado `gpt4all-installer-linux.run`.
   ![img-3](./imgs/3.png)

4. Haz clic derecho en el archivo descargado y selecciona "Propiedades" o presiona "Alt + Intro".
   ![img-4](./imgs/4.png)

5. En la ventana de propiedades, marca la opción "Permitir ejecutar el archivo como un programa".
   ![img-5](./imgs/5.png)

6. Abre una terminal desde la carpeta donde se encuentra el archivo descargado. Puedes hacerlo haciendo clic derecho en la carpeta y seleccionando "Abrir en una terminal".
   ![img-6](./imgs/6.png)

7. Instala la aplicación ejecutando el siguiente comando en la terminal:
Esto iniciará el instalador de la aplicación.
   ![img-7](./imgs/7.png)

    ```bash
    ./gpt4all-installer-linux.run
    ```

8. En la pantalla de configuración inicial, selecciona "Siguiente".
   ![img-8](./imgs/8.png)

9. Elige la carpeta de instalación y haz clic en "Siguiente".
   ![img-9](./imgs/9.png)

10. Selecciona el componente "gpt4all".
   ![img-10](./imgs/10.png)

11. Acepta la licencia y haz clic en "Siguiente".
   ![img-11](./imgs/11.png)
   ![img-12](./imgs/12.png)

12. Haz clic en "Instalar".
   ![img-13](./imgs/13.png)

    Nota: Si aparece un error durante la instalación, selecciona "Ignorar". <br>
    Este error ocurre debido a la falta de configuración del icono de inicio en Ubuntu.
   ![img-Nota](./imgs/14.png)

13. Haz clic en "Finalizar" para completar la instalación.
   ![img-15](./imgs/15.png)

    Nota 2: La aplicación se encuentra en la ubicación donde se realizó la instalación en el paso 9. En mi caso, se encuentra en home/user/gpt4all. <br>
    La aplicación está dentro de la carpeta bin/.
   ![img-15](./imgs/16.png)
    El nombre del archivo ejecutable es chat.
   ![img-17](./imgs/17.png)
    Recuerda esta ubicación para crear el icono de inicio.

### Icono en el inicio de Ubuntu

Sigue estos pasos para agregar un icono en el inicio de Ubuntu:

1. Haz clic en las tres líneas en la esquina superior derecha del administrador de archivos.
   ![img-18](./imgs/18.png)

2. Selecciona "Mostrar archivos ocultos" o presiona "Ctrl + H".
   ![img-19](./imgs/19.png)

3. Aparecerán los archivos ocultos y entra en la carpeta ".local".
   ![img-20](./imgs/20.png)

4. Dentro de la carpeta "local", entra en "share".
   ![img-21](./imgs/21.png)

5. Luego, entra en la carpeta "applications".
   ![img-22](./imgs/22.png)

6. Crea un archivo llamado "GPT4All.desktop" dentro de la carpeta "applications". Asegúrate de agregar la extensión ".desktop" al final del nombre para que sea reconocido por el sistema.
   ![img-23](./imgs/23.png)

7. Abre el archivo "GPT4All.desktop" y agrega el siguiente contenido:
Nota: Asegúrate de ajustar la ruta de acuerdo a la ubicación de tu instalación de gpt4all.
   ![img-24](./imgs/24.png)

    ```text
    [Desktop Entry]
    Type=Application
    Categories=Utility
    Name=Gpt4all
    Icon=/home/user/gpt4all/logo-32.png
    Exec=/home/user/gpt4all/bin/chat
    ```

8. Reinicia el entorno gráfico de GNOME para que el icono aparezca:
Nota: Si no funciona, reinicia el sistema por completo.
   ![img-25](./imgs/25.png) 

   ```bash
    gnome-shell --replace &
   ```

9. Si todo ha salido bien, el icono de gpt4all debería aparecer en el inicio. 
   ![img-26](./imgs/26.png)

## Configuración GPT4All Chat UI

Sigue estos pasos para configurar gpt4all en Ubuntu:

1. Haz clic en la aplicación para abrirla.
   ![img-26](./imgs/26.png)

2. La aplicación mostrará los modelos disponibles. Selecciona el que más te guste. Recuerda que puedes cambiarlo más tarde.
   ![img-27](./imgs/27.png)

3. En mi caso, seleccioné "vicuna-13b-1.1-q4_2" y "vicuna-7b-1.1-q4_2".
   ![img-28](./imgs/28.png)

4. A continuación, se abrirá un entorno similar a ChatGPT, donde puedes escribir tus preguntas y la IA responderá utilizando los recursos de tu PC.
   ![img-29](./imgs/29.png)

5. Si deseas actualizar o descargar modelos adicionales, haz clic en las tres barras diagonales para mostrar los botones correspondientes.
   ![img-30](./imgs/30.png)
   ![img-31](./imgs/31.png)

6. En nuestro caso, selecciona el icono de engranaje ("opciones").
   ![img-32](./imgs/32.png)

7. En "Application", activa el servidor web "Enable web server".
   ![img-33](./imgs/33.png)
   ![img-34](./imgs/34.png)

8. Ten en cuenta que esta opción consume una cantidad considerable de memoria RAM.

## Configuración del servidor con Python

Sigue estos pasos para configurar el servidor:

1. Verifica si tienes instalado Python 3 y pip ejecutando los siguientes comandos:
   ![img-35](./imgs/35.png)

   ```bash
   python3 --version
   pip --version
   ```

2. Si no están instalados, ejecuta el siguiente comando para instalar Python 3 y pip: 
   ![img-36](./imgs/36.png)

   ```bash
    sudo apt install python3 python3-pip
   ```

3. Luego, instala virtualenv para crear un entorno virtual donde se ejecutará el servidor: 
   ![img-37](./imgs/37.png)

   ```bash
    sudo apt install virtualenv
   ```

4. Crea el entorno virtual utilizando el siguiente comando. Puedes elegir el nombre que desees para el entorno, en este caso lo llamaremos "server":
   ![img-38](./imgs/38.png)

   ```bash
    virtualenv server
   ```

   ![img-39](./imgs/39.png)
   
   ```bash
     source server/bin/activate
   ```

5. Para salir del entorno virtual, utiliza el siguiente comando:
   
   ```bash
    deactivate
   ```

   Para volver a entrar al entorno virtual, utiliza el siguiente comando:
   
   ```bash
    source nombre_del_entorno/bin/activate
   ```

## Server con GPT4All Chat UI

Teniendo GPT4All abierto y con el entorno virtual activado, sigue estos pasos para crear un servidor:

1. Instala openai ejecutando el siguiente comando:
   ![img-40](./imgs/40.png)

   ```bash
   pip install openai
   ```

   ![img-41](./imgs/41.png)

2. Consulta básica:
    2.1. Crea un archivo llamado [BasicChat.py](https://github.com/RETBOT/ChatDynamix/blob/main/Linux/code/BasicChat.py) y coloca el siguiente código: 
       ![img-42](./imgs/42.png)

       ```python
       import openai

       openai.api_base = "http://localhost:4891/v1"
       #openai.api_base = "https://api.openai.com/v1"

       openai.api_key = "not needed for a local LLM"

       # Set up the prompt and other parameters for the API request
       prompt = "Hi"
       print(prompt)

       # Models
       # model = "gpt-3.5-turbo"
       #model = "mpt-7b-chat"
       #model = "gpt4all-j-v1.3-groovy"
       model = "vicuna-7b-1.1-q4_2"

       # Make the API request
       response = openai.Completion.create(
           model=model,
           prompt=prompt,
           max_tokens=400,
           temperature=0.7,
           top_p=0.95,
           n=1,
           echo=True,
           stream=False
       )

       # Print the generated completion
       print(response)
       ```

    2.2. y lo ejecutaremos con el siguiente comando:
       ![img-43](./imgs/43.png)
       
       ```bash
       python BasicChat.py
       ```

    2.3. y dara como resultado la siguiente consulta: 
       ![img-44](./imgs/44.png)

3. Consulta Avanzada utilizando postman: 
    3.1. Crearemos un archivo llamado [Server.py](https://github.com/RETBOT/ChatDynamix/blob/main/Linux/code/Server.py), El cual contendra el siguiente codigo:
       python Server.py
       ![img-45](./imgs/45.png)

       ```python
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

    3.2. y lo ejecutaremos con el siguiente comando:
       ![img-46](./imgs/46.png)

       ```bash
       python Server.py
       ```

    3.3. utilizando postman seleccionamremos una consulta GET:
        a la url: http://localhost:5000 o a la que le generer el paso anterior
        y dara como resultado la siguiente consulta: 
       ![img-47](./imgs/47.png)
       que en este caso es el valor que tiene por default el mensaje
    
    3.4. para utilizar el chat seleccionaremos una consulta POST: 
        a la url: http://localhost:5000 o a la que le generer el paso anterior
        en el body, seleccionamos form-data y agregaremos un nuevo valor llamado "value" y el contenido
        es el mensaje a enviar, en este caso es "Hi" y el resultado sera la respuesta generada por gpt4all
        ![img-48](./imgs/48.png)

Para mas informacion entrar a [GPT4All Chat UI Documentation](https://docs.gpt4all.io/gpt4all_chat.html)

## Server con GPT4All Python API

Teniendo el entorno virtual activado, sigue estos pasos para crear un servidor:

1. Instala gpt4all desde la terminal ejecutando el siguiente comando:
   ![img-49](./imgs/49.png)

   ```bash
   pip install gpt4all
   ```

2. Crea un archivo llamado [Server2.py](https://github.com/RETBOT/ChatDynamix/blob/main/Linux/code/Server2.py) y coloca el siguiente código: 

   ```python
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
   ```

3. Ejecuta el archivo Server2.py con el siguiente comando:
    ![img-50](./imgs/50.png)
    
    ```bash
    python Server2.py
    ```

4. Instala una biblioteca en el servidor:
    - Si deseas instalar una biblioteca por defecto, realiza una solicitud GET a la URL http://localhost:5000/install utilizando Postman.
    - Si deseas instalar una biblioteca diferente, consulta la página oficial de GPT4All para obtener una lista de bibliotecas disponibles. Luego, realiza una solicitud POST a la misma URL (http://localhost:5000/install) utilizando Postman. En el cuerpo de la solicitud, selecciona "form-data" y agrega un nuevo campo llamado "lib" con el nombre de la biblioteca que deseas instalar.
    
   ![img-51](./imgs/51.png)
   
5. Espera a que se complete la instalación de la biblioteca. Este proceso solo es necesario la primera vez que instalas una biblioteca nueva.
   ![img-52](./imgs/52.png)

6. Una vez instalada la biblioteca, puedes realizar solicitudes de chat. Abre una nueva pestaña en Postman, 
    selecciona el método POST y utiliza la URL http://localhost:5000/chat. En el cuerpo de la solicitud, selecciona "form-data" y agrega un nuevo campo llamado "value" con el mensaje que deseas enviar. Por ejemplo, utiliza "Hi". Obtendrás la respuesta generada por GPT4All.
   ![img-53](./imgs/53.png)

7. También puedes ver el mensaje en la terminal donde se está ejecutando el servidor:
   ![img-54](./imgs/54.png)

Para mas informacion entrar a [GPT4All Python API Documentation](https://docs.gpt4all.io/gpt4all_python.html)
