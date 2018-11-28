SLACK_URL = 'https://slack.com/api/'


def get_request_url(request_type, token, arg_dict=None):

    url = SLACK_URL
    # add request type
    url += request_type + '?'
    # add token
    url += 'token=' + token + '&'
    # add arg_dict info
    if arg_dict is not None:
        for name, value in arg_dict.items():
            url += name + '=' + str(value) + '&'
    # make pretty
    url += 'pretty=1'

    return url
