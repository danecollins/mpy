from pyslack import SlackClient
import os

token = os.environ['SLACK_TOKEN']

if token == '':
    print('Could not get SLACK_TOKEN')
    exit(1)

client = SlackClient(token)
client.chat_post_message('#log', "Posted from post.py: hello!", username='awrdata')
