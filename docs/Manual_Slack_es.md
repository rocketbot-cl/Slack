# Slack
  
Módulo para conectar con Slack  
  
![banner](imgs/Banner_Slack.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Como usar este modulo
  
Para hacer uso de los comandos, primero debemos conectarnos a Slack. 
1. Nos conectaremos con nuestro espacio de trabajo en el navegador web y luego entraremos al siguiente link https://api.slack.com/apps?new_classic_app=1
2. Vamos a escribir un nombre para nuestra app y luego elegimos el espacio de trabajo en el que se va a usar. Aceptamos.
3. Iremos a la pestaña OAuth & Permissions y luego nos centraremos en la sección Scopes
4. Hacemos click en el botón Add an OAuth Scope y vamos a añadir permisos para que nos quede de la siguiente manera: chat:write:bot, chat:write:user, files:write.
5. Luego más arriba en OAuth Tokens for Your Workspace tenemos que instalar la app en nuestro Workspace. Aceptamos todos los permisos y seguimos.
6. Finalmente, debemos invitar a la app en nuestro canal y podemos usar los comandos normalmente.
7. En caso de haber añadido nuevos permisos luego de realizar estos pasos, debe reinstalar la app en el workspace.


## Descripción de los comandos

### Conectar con Slack
  
Conéctese a su aplicación de Slack con su Bot Token
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token|Tienes que poner tu Bot Token aquí|xoxb-xxxxxxx-xxxxxxx-xxxxxxxxxx|
|Resultado|Devuelve True si la conexión fue exitosa, en otro caso devuelve False|result|

### Enviar mensaje
  
Envia un mensaje a un canal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del canal|Tienes que poner el ID del canal|C10000|
|Mensaje|En esta entrada tienes que poner el mensaje que quieres enviar|Hola!|
|Resultado|Devuelve True si fue exitoso, en otro caso devuelve False|result|

### Listar canales
  
Lista todos los canales con id y nombre
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Resultado|Devuelve todos los canales que existen en el espacio de trabajo.|result|

### Escuchar todos los canales
  
Escucha todos los canales y espera una respuesta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Resultado|Devuelve información sobre el mensaje que hemos captado.|result|

### Subir archivo
  
Sube un archivo a un canal con un mensaje
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del canal|Tienes que poner el ID del canal|C10000|
|Mensaje|En esta entrada tienes que poner el mensaje que quieres enviar|Hola!|
|Seleccionar un archivo|Ruta donde está el archivo|Ruta a archivo|
|Resultado|Devuelve True si fue exitoso, en otro caso devuelve False|result|
