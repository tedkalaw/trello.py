#TODO: switch to httplib2
import urllib

class TrelloInterface:
  def __init__(self, token, app_key):
    self.app_key = app_key
    self.token = token

#note:
#it should be 
#api.trello.com/queryorwhateveritis  **?key=self.app_key&token=self.token**
