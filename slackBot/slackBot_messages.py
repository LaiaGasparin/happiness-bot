"""
All functions related with the messages construction.
"""

import slackBot_globals
import json
import random

def get_data_from_json_file(file_path):
    f = open(file_path)
    data = json.load(f)
    return data

#GET MEMBERS AND COMPLIMENTS FROM JSON FILES
def gather_data(team_file = "", compliments_file = ""):
    if team_file == "":
        team_file = slackBot_globals.TEAM_FILE_PATH
    if compliments_file == "":
        compliments_file = slackBot_globals.COMPLIMENTS_FILE_PATH
    try:
        members = get_data_from_json_file(team_file)
        membersList = members["members"]
        compliments = get_data_from_json_file(compliments_file)
        complimentsList = compliments["general"]
        return membersList, complimentsList
    except:
        return [],[]

def get_random_comment(membersList = [], complimentsList = [], likelihood = 0.8):
    if slackBot_globals.LIKELIHOOD_INTEREST_COMMENT:
        likelihood = float(slackBot_globals.LIKELIHOOD_INTEREST_COMMENT)

    members_lenth = len(membersList)
    compliments_length = len(complimentsList)
    if compliments_length>0 and members_lenth>0:
        c = random.randint(0,compliments_length-1)
        m = random.randint(0,members_lenth-1)
        text = ""
        member = membersList[m]

        if random.random() > likelihood:
            text = "Rumors says you are really great at " + member["interest"] + \
             "! Wooooow. Tell us more!"
        else:
            text = complimentsList[c]

        comment = f'Hey @{member["name"]}! {text}'
    else:
        comment = "Hey there! How are you doing?"

    print(comment)
    return comment
