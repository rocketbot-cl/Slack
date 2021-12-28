import requests
from slack import RTMClient
from slack import WebClient
from slack.errors import SlackApiError
import os

def get_channel_info(channel):
    channel_info = {
        'id': channel['id'],
        'name': channel['name']
    }
    return channel_info


class SlackService:
    def __init__(self, slack_token: str):
        self.slack_token = slack_token
        self.slack_client = WebClient(token=slack_token)
        self.rtm_client = RTMClient(token=slack_token)

    def post_message(self, channel: str, text: str) -> int:
        try:
            response = self.slack_client.chat_postMessage(
                channel=channel,
                text=text
            )
            return response.status_code
        except SlackApiError as e:
            raise e
    
    def post_message_with_image(self, channel: str, text: str, image_path: str) -> int:
        try:
            with open(image_path, 'rb') as image_content:
                response = self.slack_client.files_upload(
                    channels = channel,
                    content = image_content.read(),
                    filename = image_path.split(os.sep)[-1],
                    initial_comment = text
                )
            return response.status_code
        except SlackApiError as e:
            raise e

    def list_channels(self, types : str) -> list:
        response = self.slack_client.conversations_list(types=types)
        list_channels = response.data['channels']
        list_ids = list(map(get_channel_info, list_channels))
        return list_ids


if __name__ == '__main__':
    slack_service = SlackService('xoxb-2425917630453-2436304297300-mqWaBb7VNAToVQY0FhyhbQnq')
    try:
        list_channels = slack_service.list_channels('public')
        print()
    except Exception as err:
        print(err)


# @RTMClient.run_on(event="message")
# def amusebot(**payload):
#     print(payload)
#     """
#     This function triggers when someone sends
#     a message on the slack
#     """
#     data = payload["data"]
#     web_client = payload["web_client"]
#     bot_id = data.get("bot_id", "")
#
#     # If a message is not send by the bot
#     if bot_id == "":
#         channel_id = data["channel"]
#
#         # Extracting message send by the user on the slack
#         text = data.get("text", "")
#         text = text.split(">")[-1].strip()
#
#         response = ""
#         if "help" in text.lower():
#             user = data.get("user", "")
#             response = f"Hi <@{user}>! I am AmuseBot :)"
#         else:
#             activity_json_response = requests.get("http://www.boredapi.com/api/activity/").json()
#             activity = activity_json_response['activity']
#             response = str(activity)
#
#         # Sending message back to slack
#         web_client.chat_postMessage(channel=channel_id, text=response)
#
#
# try:
#     rtm_client = RTMClient(token="xoxb-2425917630453-2436304297300-mqWaBb7VNAToVQY0FhyhbQnq")
#     print("Bot is up and running!")
#     rtm_client.start()
# except Exception as err:
#     print(err)
