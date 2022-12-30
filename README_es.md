# Slack
  
Módulo para conectar con Slack  

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


## Overview


1. Conectar con Slack  
Conéctese a su aplicación de Slack con su Bot Token

2. Enviar mensaje  
Envia un mensaje a un canal

3. Listar canales  
Lista todos los canales con id y nombre

4. Escuchar todos los canales  
Escucha todos los canales y espera una respuesta

5. Subir archivo  
Sube un archivo a un canal con un mensaje  




----
### OS

- windows
- mac
- linux

### Dependencies
- [**slack_client**](https://pypi.org/project/slack_client/)- [**slack_sdk**](https://pypi.org/project/slack_sdk/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)