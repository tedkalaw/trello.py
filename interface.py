import trello
import argparse

TEDS_KEY = '32adf82c057290a622fd71ba0638b428'
TOKEN_GENERATOR = "https://trello.com/1/connect?key=32adf82c057290a622fd71ba0638b428&name=trello%20commandline%20interface&response_type=token&context=read,write"
#Setup various args
parser = argparse.ArgumentParser(description='Commandline interface for Trello.',
                                  epilog="You can generate your user token by going to: {0}".format(TOKEN_GENERATOR))
parser.add_argument('-token', action='store', help='Your unique user token.')
args = parser.parse_args()

if args.token:
  print(args.token)

#let's start it up
