import http.client
import mimetypes
def auth_id():
  from django.conf import settings
  conn = http.client.HTTPSConnection("api.mojoauth.com")


  payload = '{'+f"\n    \"email\": \"{settings.EMAIL}\"\n"+'}'
  headers = {
    'X-API-Key': 'test-362f5f13-7aa0-4c50-bd74-bbaf140515a8',
    'Content-Type': 'application/json'
  }
  conn.request("POST", f"/users/magiclink", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  return eval(data.decode("utf-8"))["state_id"]

def is_auth(state_id):
  conn = http.client.HTTPSConnection("api.mojoauth.com")
  payload = ''
  headers = {
    'X-API-Key': 'test-362f5f13-7aa0-4c50-bd74-bbaf140515a8',
  }
  conn.request("GET", f"/users/status?state_id={state_id}", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))
  return str("{\"authenticated\":false}" != data.decode("utf-8"))