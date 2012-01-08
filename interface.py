import trello
import argparse

TEDS_KEY = '32adf82c057290a622fd71ba0638b428'
TOKEN_GENERATOR = "https://trello.com/1/connect?key={0}&name=trello%20commandline%20interface&response_type=token&context=read,write".format(TEDS_KEY)

parser = argparse.ArgumentParser(description='Commandline interface for Trello.',
                                  epilog="You can generate your user token by going to: {0}".format(TOKEN_GENERATOR))
parser.add_argument('-token', action='store', help='Your unique user token from Trello.')
args = parser.parse_args()

if args.token:
  with open('./.token', mode='w', encoding='utf-8') as store:
    store.write(args.token)

