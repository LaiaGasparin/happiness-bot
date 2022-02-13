import time
from tqdm import tqdm

import slackBot_messages
import slackBot_requests
import slackBot_globals


def wait_between_comments(time_btw):

    time.sleep(time_btw)
    return time_btw

def elapsed_time(start):
    end = time.time()
    return end - start

def doChallenge():
    start = time.time()
    CHANNEL = slackBot_globals.CHANNEL
    DURATION = int(slackBot_globals.CHALLENGE_DURATION)
    TIME_BTW = int(slackBot_globals.TIME_BETWEEN_COMMENTS)

    """ Get Team members and list of compliments from json files"""
    membersList, complimentsList = slackBot_messages.gather_data()

    """Post a comment for 2 hours"""
    with tqdm(total=DURATION) as pbar:
        while elapsed_time(start) < DURATION:
            """Get a comment combining members data and compliments list """
            comment = slackBot_messages.get_random_comment(membersList, complimentsList)
            """Post the comment to the #happy_bot_laia Slack Channel"""
            r = slackBot_requests.post_message_to_slack(CHANNEL, comment)
            """Wait 10 minutes before the next Post"""
            wait_between_comments(TIME_BTW)
            pbar.update(TIME_BTW)

def main():

    """
    Init challenge settings so you don't need to
    change Python files if parameters change.
    This way anyone can parameterize the app.
    """
    slackBot_globals.initialize()
    doChallenge()


if __name__ == "__main__":
    main()
