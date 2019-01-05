import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

api_key = 'AIzaSyBkOGG7wQiUeGfOa69eQJYSi2WLuQcbsBo'
database_url = 'https://eeel-flagger.firebaseio.com/rest/saving-data/fireblog/posts.json'

def get_access_token():
    scopes = ['https://www.googleapis.com/auth/firebase.database']

def post(data):
    headers = {"content-type": "application/json; charset=UTF-8"}
    result = requests.post(database_url,data=data,headers=headers)
    print(result)

post({'data' : 1})