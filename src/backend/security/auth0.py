import jwt
from jwt import PyJWKClient
from jwt.exceptions import InvalidKeyError, InvalidTokenError
from models.user import User
import requests

JWKS_URL = "https://dev-nlm.us.auth0.com/.well-known/jwks.json"

def get_user_info(auth_header: str):
  valid_user = True
  
  auth_token = str.split(auth_header, ' ')[1]
  jwks_client = PyJWKClient(JWKS_URL)
  signing_key = jwks_client.get_signing_key_from_jwt(auth_token)
  try:
    jwt_info = jwt.decode(auth_token, 
                          algorithms=["RS256"],
                          key=signing_key.key,
                          options={"verify_aud": False}, # Audience isn't verifying successfully, front-end not putting correct audience on the jwt or am I?
                          audience="http://localhost:8000")
  except InvalidTokenError as e:
    print(f"Token from /user/login was invalid: {e}")
    valid_user = False
  except InvalidKeyError as e:
    print(f"Key from auth0 while trying to perform /user/login was invalid: {e}")
    valid_user = False
  
  newUser = None
  if(valid_user):
    newUser = User(jwt_info['sub'].split("|")[1], jwt_info['https://foodreview.com/email'])    
  return newUser