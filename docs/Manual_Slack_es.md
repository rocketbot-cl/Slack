# Slack
  
Connect with Slack, send a listen messages  
  
![banner](imgs/Banner_Slack.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



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
