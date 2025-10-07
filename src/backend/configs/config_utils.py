import json

def get_config_as_dict(config_dir):
    config_data = None
    try:
        with open(f"{config_dir}/config.json") as f:
            config_data = json.load(f)
    except Exception as e:
        print("Error accessing/parsing the config file: ", e)
    
    return config_data
    
def get_secrets_as_dict(config_dir):
    secrets_data = None
    try:
        with open(f"{config_dir}/secrets.json") as f:
            secrets_data = json.load(f)
    except Exception as e:
        print("Error accessing/parsing the secrets file: ", e)
    
    return secrets_data

def get_postgres_server_details(config_dir):
    config_data = get_config_as_dict(config_dir)
    secrets_data = get_secrets_as_dict(config_dir)
    
    # Database configuration
    postgres_details = {}
    postgres_details["host"] = "localhost"
    postgres_details["port"] = "9999"
    postgres_details["username"] = "postgres"
    postgres_details["password"] = "password"
    if(config_data != None and secrets_data != None):
        postgres_details["host"] = config_data["postgres_server"]["host"]
        postgres_details["port"] = config_data["postgres_server"]["port"]
    if(secrets_data != None):
        postgres_details["username"] = secrets_data["postgres_server"]["username"]
        postgres_details["password"] = secrets_data["postgres_server"]["password"]
        
    return postgres_details