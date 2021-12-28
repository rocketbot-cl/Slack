



# Slack
  
Connect with Slack, send a listen messages  
  
![banner](https://i.imgur.com/5F1NYSl.jpg)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.
## Como usar este modulo
  
Para hacer uso de los comandos, primero debemos conectarnos a Slack. 
1. Nos conectaremos con nuestro espacio de trabajo en el navegador web y luego entraremos al siguiente link https://api.slack.com/apps?new_classic_app=1
2. Vamos a escribir un nombre para nuestra app y luego elegimos el espacio de trabajo en el que se va a usar. Aceptamos.
3. Iremos a la pestaña OAuth & Permissions y luego nos centraremos en la sección Scopes
4. Hacemos click en el botón Add an OAuth Scope y vamos a añadir permisos para que nos quede de la siguiente manera: chat:write:bot, chat:write:user, files:write.
5. Luego más arriba en OAuth Tokens for Your Workspace tenemos que instalar la app en nuestro Workspace. Aceptamos todos los permisos y seguimos.
6. Finalmente, debemos invitar a la app en nuestro canal y podemos usar los comandos normalmente.

## Descripción de los comandos

### Conectar con Slack
  
Conectar con Slack
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token|You have to put your Bot Token here|xoxb-xxxxxxx-xxxxxxx-xxxxxxxxxx|
|Resultado|Return True if the connection was succesful, in other case return False|result|

### Enviar mensaje
  
Envia un mensaje a un canal
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del canal|You have to put the ID channel|C10000|
|Mensaje|In this input you have to put the message that you want to send|Hola!|
|Resultado|Return True if the connection was succesful, in other case return False|result|

### Listar canales
  
Lista todos los canales con id y nombre
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Resultado|Return all the channels that exist in workspace|result|

### Escuchar todos los canales
  
Escucha todos los canales y espera una respuesta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Resultado|Return information about the message that we have catched.|result|
