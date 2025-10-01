# Running the Backend
The backend should always be run from main.py. Utility scripts can be run via command line arguments, use -h for details.

# CONFIGS
The backend files assume the existence of a config.json containing the host and port of your postgres file. They also assume a secrets.json containing the username and password for your postgres file.

# MIGRATIONS
The migrations directory contains a script to fill necessary tables in your database. It can be run with the -m argument on main.py