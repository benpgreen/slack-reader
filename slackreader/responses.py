import datetime as dt


class User:

    def __init__(self, user_response):

        self.id = user_response['id']
        self.slack_name = user_response['name']
        self.real_name = user_response['real_name']
        self.bot = user_response['is_bot']


class Channel:

    def __init__(self, channel_response):

        self.id = channel_response['id']
        self.name = channel_response['name']
        self.created_ts = channel_response['created']
        self.created_utc = dt.datetime.utcfromtimestamp(self.created_ts)
        self.archived = channel_response['is_archived']
        self.creator_id = channel_response['id']
        self.private = channel_response['is_private']
        self.num_members = channel_response['num_members']
