import urllib

class TrelloInterface:
  def __init__(self, token, app_key):
    #will need to figure out what the proper thing to do with this is
    self.app_key = app_key
    self.token = token

#    self.token = "2869245a05aaff93daf7a044e2ceb3b9"
    
#note:
#it should be 
#api.trello.com/queryorwhateveritis  **?key=self.app_key&token=self.token**
