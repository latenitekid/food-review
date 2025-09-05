from models.user import NewUser
from sqlalchemy import create_engine, text

engine  = create_engine("postgresql://foodreview:password@localhost:9999/foodreview")

def add_user(user: NewUser):
  with engine.connect() as conn:
    conn.execute(
      text("""
        INSERT INTO users
          (user_id, username, encrypted_pass)
        VALUES
          (1, :username, :encrypted_pass)
        """
      ),
      {
        "username": user.username,
        "encrypted_pass": user.encrypted_pass
      }
    )

    conn.commit()
    
def change_user_password(user_id: int, new_encrypted_pass: str):
  with engine.connect() as conn:
    conn.execute(
      text("""
        UPDATE users
        SET encrypted_pass = :new_encrypted_pass
        WHERE user_id = :user_id
        """
      ),
      {
        "user_id": user_id,
        "encrypted_pass": new_encrypted_pass
      }
  )

  conn.commit()
  
def change_user_username(user_id: int, new_username: str):
  with engine.connect() as conn:
    conn.execute(
      text("""
        UPDATE users
        SET username = :new_username
        WHERE user_id = :user_id
        """
      ),
      {
        "user_id": user_id,
        "encrypted_pass": new_username
      }
  )

  conn.commit()