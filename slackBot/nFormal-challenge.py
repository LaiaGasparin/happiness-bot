import json
import random
import time
import requests


 #GLOBAL VARIABLES

complimentsList = []
membersList = []


def get_data_from_json_file(file_path):
    f = open(file_path)
    data = json.load(f)
    return data

#GET MEMBERS AND COMPLIMENTS FROM JSON FILES
def gather_data(team_file = TEAM_FILE_PATH, compliments_file = COMPLIMENTS_FILE_PATH):
  global complimentsList, membersList
  members = get_data_from_json_file(team_file)
  membersList = members["members"]
  compliments = get_data_from_json_file(compliments_file)
  complimentsList = compliments["general"]

def get_random_comment(membersList = [], complimentsList = [], likelihood = 0.8):
  members_lenth = len(membersList)
  compliments_length = len(complimentsList)
  if compliments_length>0 and members_lenth>0:
    c = random.randint(0,compliments_length-1)
    m = random.randint(0,members_lenth-1)
    text = ""
    member = membersList[m]

    if random.random() > likelihood:
      text = "Rumors says you are really great at " + member["interest"] + "! Wooooow. Tell us more!"
    else:
      text = complimentsList[c]

    comment = f'Hey @{member["name"]}! {text}'
  else:
    comment = "Hey there! How are you doing?"
  return comment

def post_message_to_slack(token, channel, text):
  CHAT_POST_MSG_URL = 'https://slack.com/api/chat.postMessage'
  auth = 'Bearer ' + BOT_TOKEN
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
      




gather_data()

start = time.time()
elapsed = 0
while elapsed < TWO_HOUR_IN_SECONDS:
  comment = get_random_comment(membersList, complimentsList, LIKELIHOOD_INTEREST_COMMENT)
  print(comment)
  r = post_message_to_slack(BOT_TOKEN, CHANNEL, comment)
  print(r)
  time.sleep(TIME_BETWEEN_COMMENTS)
  end = time.time()
  elapsed = end - start

print(elapsed)
