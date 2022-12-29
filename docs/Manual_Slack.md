



# Slack
  
Connect with Slack, send a listen messages  
  
![banner](imgs/Banner_Slack.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connect with Slack
  
Connect to your Slack App using your Bot Token
|Parameters|Description|example|
| --- | --- | --- |
|Token|You have to put your Bot Token here|xoxb-xxxxxxx-xxxxxxx-xxxxxxxxxx|
|Result|Returns True if the connection was succesful, in other case return False|result|

### Send message
  
Send a message to a channel
|Parameters|Description|example|
| --- | --- | --- |
|Channel ID|You have to put the ID channel|C10000|
|Message|In this input you have to put the message that you want to send|Hola!|
|Result|Returns True if it was succesful, in other case return False|result|

### List channels
  
List all the channels with id and name
|Parameters|Description|example|
| --- | --- | --- |
|Result|Returns every channel that exists in workspace|result|

### Listen channels
  
Listen for all channel and wait a response
|Parameters|Description|example|
| --- | --- | --- |
|Result|Returns information about the message that we have catched.|result|
