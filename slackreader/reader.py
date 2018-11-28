import requests

SLACK_URL = 'https://slack.com/api/'


class SlackReader:

    def __init__(self, API_KEY):
        self.api_key = API_KEY

    def get_users(self, active_only=True):

        url = SLACK_URL + "users.list?token={}&pretty=1"
        response = requests.get(url.format(self.api_key))
        response = response.json()
        if not response['ok']:
            raise ValueError("Problem connecting.")
        user_list = []
        for user in response['members']:
            if not user['deleted'] or not active_only:
                user_list.append(user['id'])
        self.users = user_list

    def get_channels(self):

        url = SLACK_URL + "channels.list?token={}&pretty=1"
        response = requests.get(url.format(self.api_key))
        response = response.json()
        if not response['ok']:
            raise ValueError("Problem connecting.")
        channel_list = []
        for channel in response['channels']:
            if channel['is_channel']:
                channel_list.append(channel['id'])
        self.channels = channel_list
