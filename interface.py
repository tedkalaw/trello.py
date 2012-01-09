import trello
import argparse

TEDS_KEY = '32adf82c057290a622fd71ba0638b428'
TOKEN_GENERATOR = "https://trello.com/1/connect?key={0}&name=trello%20commandline%20interface&response_type=token&context=read,write".format(TEDS_KEY)

parser = argparse.ArgumentParser(description='Commandline interface for Trello.',
                                  epilog="You can generate your user token by going to: {0}".format(TOKEN_GENERATOR))
parser.add_argument('-token', action='store', help='Your unique user token from Trello.')
parser.add_argument('--t', action='store_true', help='Display token')
args = parser.parse_args()

if args.token:
  with open('.token', mode='w', encoding='utf-8') as store:
    store.write(args.token)
    print("Successfuly stored token.")

try:
  _token_file = open('.token', encoding='utf-8')
except IOError:
  print("You need to add your user token.\nThis can be generated at:\n{0}".format(TOKEN_GENERATOR))

token = _token_file.read()
_token_file.close()

if args.t:
  print('Your token is:\n{0}'.format(token))
  exit()

ti = trello.TrelloInterface(TEDS_KEY, token)
print(ti.request_url('members/me/cards'))
for board in ti.boards():
  print(board.lists())
