



# Slack
  
Module to connect with Slack.  

*Read this in other languages: [English](Manual_Slack.md), [Português](Manual_Slack.pr.md), [Español](Manual_Slack.es.md)*
  
![banner](imgs/Banner_Slack.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
  
To make use of the commands, we must first connect to Slack. 
1. We will connect to our workspace in the web browser and then we will enter the following link https://api.slack.com/apps?new_classic_app=1
2. We will write a name for our app and then choose the workspace in which it will be used. We accept.
3. We will go to the OAuth & Permissions tab and then we will focus on the Scopes section.
4. We click on the Add an OAuth Scope button and we will add permissions so that it looks like this: chat:write, files:write, channels:write.invites, groups:write.nvites, channels:manage, mpim:write, im:write, groups:write.
5. Then further up in OAuth Tokens for Your Workspace we have to install the app in our Workspace. We accept all the permissions and continue.
6. Finally, we have to invite the app in our channel and we can use the commands normally.
7. In case you have added new permissions after these steps, you must reinstall the app in the workspace.


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

### Upload file
  
Upload a file to a channel with a message
|Parameters|Description|example|
| --- | --- | --- |
|Channel ID|You have to put the ID channel|C10000|
|Message|In this input you have to put the message that you want to send|Hola!|
|Select a file|Path where the file is|Path to file|
|Result|Returns True if it was succesful, in other case return False|result|

### Invite User
  
Invite user to a channel
|Parameters|Description|example|
| --- | --- | --- |
|Channel ID|You have to put the ID channel|C10000|
|User ID|You have to put the ID user|U07EW8KLMAS|
|Result|Returns True if it was succesful, in other case return False|result|

### Delete User
  
Removes a user from a conversation
|Parameters|Description|example|
| --- | --- | --- |
|Channel ID|You have to put the ID channel|C10000|
|User ID|You have to put the ID user|U07EW8KLMAS|
|Result|Returns True if it was succesful, in other case return False|result|
