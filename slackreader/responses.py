import requests
import datetime as dt

from .tools import get_request_url


class User:

    def __init__(self, token, user_response):

        self.id = user_response['id']
        self.slack_name = user_response['name']
        self.real_name = user_response['real_name']
        self.bot = user_response['is_bot']
        self.token = token

    def __repr__(self):
        return 'User: ' + self.real_name


class Message:

    def __init__(self, message_response):

        self.user = message_response['user']
        self.text = message_response['text']
        self.created_ts = float(message_response['ts'])
        self.created_utc = dt.datetime.utcfromtimestamp(self.created_ts)
        if 'reactions' in message_response.keys():
            self.reactions = message_response['reactions']
        else:
            self.reactions = []

    def __repr__(self):
        return 'Message: ' + self.text


class Channel:

    def __init__(self, token, channel_response):

        self.id = channel_response['id']
        self.name = channel_response['name']
        self.created_ts = channel_response['created']
        self.created_utc = dt.datetime.utcfromtimestamp(self.created_ts)
        self.archived = channel_response['is_archived']
        self.creator_id = channel_response['id']
        self.private = channel_response['is_private']
        self.num_members = channel_response['num_members']
        self.token = token

    def __repr__(self):
        return 'Channel: ' + self.name

    def get_messages(self, oldest=None, latest=None):

        arg_dict = {'channel': self.id}

        if isinstance(oldest, dt.datetime):
            arg_dict['oldest'] = oldest.timestamp()
        elif isinstance(oldest, (int, float)):
            arg_dict['oldest'] = oldest
        elif oldest is not None:
            msg = '`oldest` must be None, dt.datetime, int, or float - not {}'
            raise TypeError(msg.format(type(oldest)))

        if isinstance(latest, dt.datetime):
            arg_dict['latest'] = latest.timestamp()
        elif isinstance(latest, (int, float)):
            arg_dict['latest'] = latest
        elif oldest is not None:
            msg = '`latest` must be None, dt.datetime, int, or float - not {}'
            raise TypeError(msg.format(type(latest)))

        has_more = True
        messages = []
        while has_more:
            url = get_request_url(
                        'channels.history',
                        self.token,
                        arg_dict=arg_dict
                        )
            response = requests.get(url)
            response = response.json()
            if not response['ok']:
                raise RuntimeError("Problem connecting.")
            for message in response['messages']:
                if 'user' in message.keys():
                    messages.append(Message(message))
                last_ts = message['ts']

            arg_dict['latest'] = last_ts
            has_more = response['has_more']

        self.messages = messages
