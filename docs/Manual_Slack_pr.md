



# Slack
  
Connect with Slack, send a listen messages  
  
![banner](imgs/Banner_Slack.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



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
