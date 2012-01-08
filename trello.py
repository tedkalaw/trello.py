import httplib2

class TrelloInterface:
  def __init__(self, app_key, token):
    self.app_key = app_key
    self.token = token

  def request_url(action)
    return 'api.trello.com/{0}?key={1}&token={2}'.format(action, self.app_key, self.token)
  end
