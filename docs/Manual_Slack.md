



# Slack
  
Connect with Slack, send a listen messages  
  
![banner](/docs/imgs/Banner_Slack.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



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

### Subir archivo
  
Sube un archivo a un canal con un mensaje
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del canal|Tienes que poner el ID del canal|C10000|
|Mensaje|En esta caja de texto tienes que poner el mensaje que quieres enviar|Hola!|
|Seleccionar un archivo|Ruta donde está el archivo|Ruta a archivo|
|Resultado|Devuelve True si la conexión fue exitosa, en otro caso devuelve False|result|
