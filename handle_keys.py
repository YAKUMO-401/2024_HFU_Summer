import os,sys

def get_secret_and_token():

    channel_secret = os.getenv('LINEBOT_SECRET_KEY', None)
    channel_access_token = os.getenv('LINEBOT_ACCESS_TOKEN', None)
    if channel_secret is None:
        print('Specify LINEBOT_SECRET_KEY as environment variable.')
        sys.exit(1)
    if channel_access_token is None:
        print('Specify LINEBOT_ACCESS_TOKEN as environment variable.')
        sys.exit(1)

    return {
        'LINEBOT_SECRET_KEY':channel_access_token,
        'LINEBOT_ACCESS_TOKEN':channel_access_token
    }