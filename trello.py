import httplib2
import json
from urllib.parse import urlencode

#Do we care what the url is? Maybe it makes more sense if it's queried for
#Same with checking if something is closed, perhaps...
class TrelloInterface:
  def __init__(self, app_key, token):
    self.app_key = app_key
    self.token = token
    self.h = httplib2.Http('.cache')

  def request_url(self, action, options = {}):
    return 'https://api.trello.com/1/{0}?{1}&key={2}&token={3}'.format(action, urlencode(options), self.app_key, self.token)

  #Add in caching
  def api_request(self, url, action, options):
    '''Returns decoded JSON returned after hitting url with action'''
    url = self.request_url(url, options)
    response, content = self.h.request(url, action, headers = {'Accept': 'application/json'})
    if response != 200:
      #TODO: figure out what exception goes here
      pass
    
    return json.loads(content.decode('utf-8'))

  def boards(self, options = {}):
    '''Returns list of boards associated with current token'''
    boards_json = self.api_request('members/me/boards', 'GET', options)
    boards = list()
    for board in boards_json:
      boards.append(Board(self, board['id'], board['name'], board['closed'], board['url']))
    return boards

  def feed(self):
    #it's at /card/:id/actions (card activity) or /board/:id/actions (activity for the board)
    pass

#TODO: subclass all types
class Board:
  def __init__(self, interface, board_id, name, closed, url):
    self.id = board_id
    self.name = name
    self.closed = closed
    self.url = url
    self.interface = interface

  def lists(self, options = {}):
    '''Returns list of lists associated with this board'''
    lists_json = self.interface.api_request('boards/{0}/lists'.format(self.id), 'GET', options)
    print(lists_json)
    lists = list()
    for list_object in lists_json:
      lists.append(List(self.interface, list_object['name'], list_object['closed'],
        list_object['id']))

#It's better to query for cards separately, since they can be changed so quickly
class List:
  #cards is a dict
  def __init__(self, interface, name, closed, id):
    self.interface = interface
    self.name = name
    self.closed = closed
    self.id = id

class Card:
  #TODO: add in badges - these are the interesting things
  def __init__(self, interface, name, desc, closed):
    self.interface = interface
    self.name = name
    self.desc = desc
    self.closed = closed

class Checklist:
  pass
