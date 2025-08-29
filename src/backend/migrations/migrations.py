from configs.config_utils import get_postgres_server_details
from datetime import datetime
import os
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, DateTime
from sqlalchemy.exc import ProgrammingError
import sys

postgres_details = get_postgres_server_details("../../../config")
  
DB_URL = f"postgresql://{postgres_details['username']}:{postgres_details['password']}@{postgres_details['host']}:{postgres_details['port']}/foodreview"

def create_migration_table(engine):
    """Create the migration_scripts table if it doesn't exist."""
    metadata = MetaData()
    
    # Define the migration_scripts table
    Table('migration_scripts', metadata,
          Column('script_name', String, primary_key=True),
          Column('executed_at', DateTime, nullable=False)
    )
    
    # Create the table
    try:
        metadata.create_all(engine)
        print("Created migration_scripts table")
    except Exception as e:
        print(f"Error creating migration_scripts table: {e}")
        sys.exit(1)

def get_executed_scripts(engine):
    """Get list of already executed migration scripts."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT script_name FROM migration_scripts"))
            return {row[0] for row in result}
    except ProgrammingError:
        # Table doesn't exist yet
        create_migration_table(engine)
        return set()
    except Exception as e:
        print(f"Error getting executed scripts: {e}")
        sys.exit(1)

def execute_migration(engine, script_path, script_name):
    """Execute a single migration script and record its execution."""
    try:
        # Read the SQL script
        with open(script_path, 'r') as f:
            sql = f.read()
        
        # Execute the script and record it in a transaction
        with engine.begin() as conn:
            # Execute the migration script
            conn.execute(text(sql))
            
            # Record the execution
            conn.execute(
                text("INSERT INTO migration_scripts (script_name, executed_at) VALUES (:name, :time)"),
                {"name": script_name, "time": datetime.now()}
            )
            
        print(f"Successfully executed {script_name}")
        return True
    except Exception as e:
        print(f"Error executing {script_name}: {e}")
        return False

def main():
    try:
        # Create database engine
        engine = create_engine(DB_URL)
        
        # Get list of executed scripts
        executed_scripts = get_executed_scripts(engine)
        
        # Get all .sql files in the migrations directory
        migration_dir = os.path.dirname(os.path.abspath(__file__))
        sql_files = [f for f in os.listdir(migration_dir) if f.endswith('.sql')]
        sql_files.sort()  # Sort by filename (which starts with date)
        
        # Execute pending migrations
        executed_count = 0
        for script_name in sql_files:
            if script_name not in executed_scripts:
                script_path = os.path.join(migration_dir, script_name)
                if execute_migration(engine, script_path, script_name):
                    executed_count += 1
        
        if executed_count == 0:
            print("No new migrations to execute")
        else:
            print(f"Successfully executed {executed_count} migration(s)")
            
    except Exception as e:
        print(f"Migration failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
