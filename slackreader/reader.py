import requests


class SlackReader:

    def __init__(self, API_KEY):
        self.api_key = API_KEY

    def get_users(self, active_only=True):

        url = "https://slack.com/api/users.list?token={}&pretty=1"
        users_response = requests.get(url.format(self.api_key))
        users = users_response.json()
        if not users['ok']:
            raise ValueError("Problem connecting.")
        user_list = []
        for user in users['members']:
            if not user['deleted'] or not active_only:
                user_list.append(user['id'])
        self.users = user_list
