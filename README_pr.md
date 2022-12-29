# Slack
  
Módulo para conectar com Slack  

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  


## Como usar este módulo

Para hacer uso de los comandos, primero debemos conectarnos a Slack.
1. Nos conectaremos a nuestro espacio de trabajo en el navegador web y luego ingresaremos al siguiente enlace https://api.slack.com/apps?new_classic_app=1
2. Escribiremos un nombre para nuestra aplicación y luego elegiremos el espacio de trabajo en el que se utilizará. Aceptamos.
3. Iremos a la pestaña OAuth & Permissions y luego nos enfocaremos en la sección Scopes.
4. Damos clic en el botón Add an OAuth Scope y agregaremos permisos para que quede así: chat:write:bot, chat:write:user, files:write.
5. Luego, más arriba en Tokens OAuth para su espacio de trabajo, tenemos que instalar la aplicación en nuestro espacio de trabajo. Aceptamos todos los permisos y continuamos.
6. Finalmente, tenemos que invitar a la aplicación en nuestro canal y podemos usar los comandos normalmente.
7. En caso de que haya agregado nuevos permisos después de estos pasos, debe volver a instalar la aplicación en el espacio de trabajo.


## Overview


1. Conectar com Slack  
Conecte-se ao seu aplicativo Slack com seu Bot Token

2. Enviar mensagem  
Enviar uma mensagem para um canal

3. Listar canais  
Listar todos os canais com id e nome

4. Ouvir todos os canais  
Ouça todos os canais e aguarde uma resposta

5. Subir arquivo  
Carregar um arquivo para um canal com uma mensagem  




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