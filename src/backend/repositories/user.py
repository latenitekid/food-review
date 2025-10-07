from configs.config_utils import get_postgres_server_details
from security.auth0 import get_user_info
from sqlalchemy import create_engine, text

postgres_details = get_postgres_server_details("../../config")
  
engine  = create_engine(f"postgresql://{postgres_details['username']}:{postgres_details['password']}@{postgres_details['host']}:{postgres_details['port']}/foodreview")

def add_user(auth_header: str):
  newUser = get_user_info(auth_header)
  if(newUser == None):
    return False

  with engine.connect() as conn:
    conn.execute(
      text("""
        INSERT INTO users
          (auth_sub, username)
        VALUES
          (:auth_sub, :username)
        ON CONFLICT (auth_sub) DO NOTHING
        """
      ),
      {
        "auth_sub": newUser.auth_sub,
        "username": newUser.username
      }
    )

    conn.commit()
    
    return True