"""
All functions related with the Slack connection
"""

import slackBot_globals
import requests
import json

def post_message_to_slack(channel, text):
    CHAT_POST_MSG_URL = slackBot_globals.CHAT_POST_MSG_URL
    auth = 'Bearer ' + slackBot_globals.BOT_TOKEN
    headers = {'Content-type': 'application/json', 'Authorization' : auth }
    payload = {
      "channel": channel,
      "text": text
    }
    try:
        payload_str = json.dumps(payload,ensure_ascii=True).encode("utf-8")
        r = requests.post(CHAT_POST_MSG_URL, data=payload_str, headers=headers)
        if r.status_code == 200:
            print(r.text)
        else:
            print("An error occurred, code={}".format(r.status_code))
    except requests.exceptions.RequestException as error:
        print(f'Error: {error}')
