# Slack
  
Module to connect with Slack  

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module
  
To make use of the commands, we must first connect to Slack. 
1. We will connect to our workspace in the web browser and then we will enter the following link https://api.slack.com/apps?new_classic_app=1
2. We will write a name for our app and then choose the workspace in which it will be used. We accept.
3. We will go to the OAuth & Permissions tab and then we will focus on the Scopes section.
4. We click on the Add an OAuth Scope button and we will add permissions so that it looks like this: chat:write:bot, chat:write:user, files:write.
5. Then further up in OAuth Tokens for Your Workspace we have to install the app in our Workspace. We accept all the permissions and continue.
6. Finally, we have to invite the app in our channel and we can use the commands normally.
7. In case you have added new permissions after these steps, you must reinstall the app in the workspace.


## Overview


1. Connect with Slack  
Connect to your Slack App using your Bot Token

2. Send message  
Send a message to a channel

3. List channels  
List all the channels with id and name

4. Listen channels  
Listen for all channel and wait a response

5. Upload file  
Upload a file to a channel with a message  




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