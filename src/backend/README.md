# CONFIGS
The backend files assume the existence of a config.json containing the host and port of your postgres file. They also assume a secrets.json containing the username and password for your postgres file.

# MIGRATIONS
The migrations directory contains a script to fill necessary tables in your database. It assumes a database named 'foodreview' exists. It should be run from inside the migrations directory.