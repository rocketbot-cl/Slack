# Slack
  
Módulo para conectar com Slack  
  
![banner](imgs/Banner_Slack.png)
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


## Descrição do comando

### Conectar com Slack
  
Conecte-se ao seu aplicativo Slack com seu Bot Token
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Token|Você tem que colocar seu Bot Token aqui|xoxb-xxxxxxx-xxxxxxx-xxxxxxxxxx|
|Resultado|Retorna True se a conexão foi bem-sucedida, caso contrário, retorna False|result|

### Enviar mensagem
  
Enviar uma mensagem para um canal
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do canal|Você tem que colocar o ID do canal|C10000|
|Mensagem|Nesta entrada você deve colocar a mensagem que deseja enviar|Hola!|
|Resultado|Retorna True se foi bem-sucedido, caso contrário, retorna False|result|

### Listar canais
  
Listar todos os canais com id e nome
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Resultado|Retorne todos os canais existentes no espaço de trabalho|result|

### Ouvir todos os canais
  
Ouça todos os canais e aguarde uma resposta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Resultado|Retorna informações sobre a mensagem que capturamos.|result|

### Subir arquivo
  
Carregar um arquivo para um canal com uma mensagem
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do canal|Você tem que colocar o ID do canal|C10000|
|Mensagem|Nesta entrada você deve colocar a mensagem que deseja enviar|Hola!|
|Selecione um arquivo|Caminho onde está o arquivo|Caminho para arquivo|
|Resultado|Retorna True se foi bem-sucedido, caso contrário, retorna False|result|
