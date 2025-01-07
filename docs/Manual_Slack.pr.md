



# Slack
  
Módulo para conectar con Slack.  

*Read this in other languages: [English](Manual_Slack.md), [Português](Manual_Slack.pr.md), [Español](Manual_Slack.es.md)*
  
![banner](imgs/Banner_Slack.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

Para hacer uso de los comandos, primero debemos conectarnos a Slack.
1. Nos conectaremos a nuestro espacio de trabajo en el navegador web y luego ingresaremos al siguiente enlace https://api.slack.com/apps?new_classic_app=1
2. Escribiremos un nombre para nuestra aplicación y luego elegiremos el espacio de trabajo en el que se utilizará. Aceptamos.
3. Iremos a la pestaña OAuth & Permissions y luego nos enfocaremos en la sección Scopes.
4. Damos clic en el botón Add an OAuth Scope y agregaremos permisos para que quede así: chat:write, files:write, channels:write.invites, groups:write.nvites, channels:manage, mpim:write, im:write, groups:write.
5. Luego, más arriba en Tokens OAuth para su espacio de trabajo, tenemos que instalar la aplicación en nuestro espacio de trabajo. Aceptamos todos los permisos y continuamos.
6. Finalmente, tenemos que invitar a la aplicación en nuestro canal y podemos usar los comandos normalmente.
7. En caso de que haya agregado nuevos
 permisos después de estos pasos, debe volver a instalar la aplicación en el espacio de trabajo.
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

### Adicionar usuário
  
Adicionar usuário a um canal
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do canal|Você tem que colocar o ID do canal|C10000|
| ID do Usuário|Você precisa colocar o ID do usuário|U07EW8KLMAS|
|Resultado|Retorna True se foi bem-sucedido, caso contrário, retorna False|result|
