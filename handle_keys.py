import os,sys

def get_secret_and_token():
        tokens_name = [
        'LINEBOT_SECRET_KEY',
        'LINEBOT_ACCESS_TOKEN',
        "OPENAI_API_KEY",
        "CWA_API_KEY"
    ]

        keys = dict()
        for token_name in tokens_name:
            token = os.getenv(token_name, None)
            if token is None:
                print(f'Specify {token_name} as environment variable.')
                sys.exit(1)
            keys[token_name] = token
            
        return keys

if __name__ == "__main__":
    keys = get_secret_and_token()
    print(keys["LINEBOT_ACCESS_TOKEN"])