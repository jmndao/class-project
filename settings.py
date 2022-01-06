import os


# Dont't change this variable it points the base directory
# that is the root of this where this settings.py file is 
# currently located
BASE_DIR = os.path.normpath(os.getcwd())

# Configuration section for the database management
# can select between available database 
DB_CONFIG = {
    "sqlite": {
        "filename": "example.db"
    },
    "mysql": {
        # Not yet implemented
    }
}
