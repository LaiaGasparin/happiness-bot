from configparser import ConfigParser

TEAM_FILE_PATH = ""
COMPLIMENTS_FILE_PATH = ""
CHALLENGE_DURATION = 0
TIME_BETWEEN_COMMENTS = 0
LIKELIHOOD_INTEREST_COMMENT = 0
BOT_TOKEN = "0"
CHANNEL = ""
CHAT_POST_MSG_URL = ""


def initialize():
    """Initialize Global Variables"""
    global TEAM_FILE_PATH,\
        COMPLIMENTS_FILE_PATH,\
        TIME_BETWEEN_COMMENTS,\
        LIKELIHOOD_INTEREST_COMMENT,\
        BOT_TOKEN,\
        CHANNEL,\
        CHAT_POST_MSG_URL,\
        CHALLENGE_DURATION

    config = ConfigParser()
    config.read('slackBot/slackBot_config.ini')

    TEAM_FILE_PATH = config['DEFAULT']['TEAM_FILE_PATH']
    COMPLIMENTS_FILE_PATH = config['DEFAULT']['COMPLIMENTS_FILE_PATH']
    CHALLENGE_DURATION = config['DEFAULT']['CHALLENGE_DURATION']
    TIME_BETWEEN_COMMENTS = config['DEFAULT']['TIME_BETWEEN_COMMENTS']
    LIKELIHOOD_INTEREST_COMMENT = config['DEFAULT']['LIKELIHOOD_INTEREST_COMMENT']
    BOT_TOKEN = config['DEFAULT']['BOT_TOKEN']
    CHANNEL = config['DEFAULT']['CHANNEL']
    CHAT_POST_MSG_URL = config['DEFAULT']['CHAT_POST_MSG_URL']

    print(CHALLENGE_DURATION)