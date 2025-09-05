from datetime import date
from pydantic import BaseModel
from .model_utils import to_camel

class NewUser(BaseModel):
  class Config:
    validate_by_name = True
    alias_generator = to_camel

  user_id: int
  username: str
  encrypted_pass: str