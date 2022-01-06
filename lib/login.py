# Login Class
# This python library use the hash md5 in order to securely save users
# login credential in the local database.

class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_user(self):
        '''
            This method checks if the user exist in the database or not.
        '''
        


    def retrieve_user_password(self):
        '''
            This function allow to retrieve the user password in the database
        '''

    def check_password(self):
        '''
            Here we check the password by retrieving the one the user has 
            been registered with.
            Thanks to md5 pythonic library we can compare the input password
            to the one we have retrieved from the database
        '''
