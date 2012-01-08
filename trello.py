import httplib2
#Response headers are STRING
#Content body is BYTES

class TrelloInterface:
  def __init__(self, app_key, token):
    self.app_key = app_key
    self.token = token
    self.h = httplib2.Http('.cache')

  def request_url(self, action):
    return 'https://api.trello.com/1/{0}?key={1}&token={2}'.format(action, self.app_key, self.token)

class Board:
  pass

class List:
  pass

class Card:
  pass

class Checklist:
  pass

class Member:
  pass
