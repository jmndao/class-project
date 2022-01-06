# This class deal with the sqlite database and implement
# all the CRUD operations
# - User: 
#       - Read user info
#       - Create a new user
#       - Update user info
#       - Update user password
#       - Delete a user

import os
import sqlite3 as sql
from DAUSTSMS.settings import *


class SQliteManager:

    def __init__(self, conn):
        '''
            Here we initialize the connection to the databse
            at init time of the database for the database instance
            to be used during this class usage.
        '''
        sql_base_file = DB_CONFIG["sqlite"]["filename"]
        conn = sql.connect(os.path.normpath(os.path.join(BASE_DIR, sql_base_file)))
        # Cursor which to use alongside to query into the database
        self._cur = conn.cursor()

    
    



    def check_user(self, username):
        pass