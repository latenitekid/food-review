class User():
  def __init__(self, auth_sub, username): # Can add user_id as optional later if we want to pass that around, but for now it's in the way because only the database can assign it
    self.auth_sub = auth_sub
    self.username = username