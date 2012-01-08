import httplib2
import json
from urllib.parse import urlencode
#Response headers are STRING
#Content body is BYTES

class TrelloInterface:
  def __init__(self, app_key, token):
    self.app_key = app_key
    self.token = token
    self.h = httplib2.Http('.cache')

  def request_url(self, action, options = {}):
    return 'https://api.trello.com/1/{0}?{1}&key={2}&token={3}'.format(action, urlencode(options), self.app_key, self.token)

  def boards(self, options = {}):
    '''Returns list of boards associated with current token'''
    url = self.request_url('members/me/boards', options)
    response, content = self.h.request(url, 'GET', headers = {'Accept': 'application/json'})
    if response != 200:
      #figure out which exception goes here
      pass

    boards_json = json.loads(content.rstrip().decode('utf-8'))
    boards = list()
    for board in boards_json:
      print(board['name'])

class Board:
  def __init__(self):
    pass

class List:
  pass

class Card:
  pass

class Checklist:
  pass

