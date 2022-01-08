# This class deal with the sqlite database and implement
# all the CRUD operations
# - User:
#       - Read user info
#       - Create a new user
#       - Update user info
#       - Update user password
#       - Delete a user

import asyncio
from pymongo import MongoClient
# from DAUSTSMS.settings import *


class MongoManager:

    __levels = [
        {
            "name": "freshman_one",
            "courses": [
                "Comp 1",
                "Calculus 1",
                "Physic 1",
                "Introduction to engineering",
                "Biology",
                "Chemistry"
            ]
        },
        {
            "name": "freshman_two",
            "courses": [
                "Comp 2",
                "Calculus 2",
                "Physic 2",
                "Algorithm"
            ]
        },
        {
            "name": "sophomore_one",
            "courses": [
                "Pop culture",
                "Calculus 3",
                "Magnetism",
                "Optic 1",
                "Introduction to engineering"
            ]
        },
        {
            "name": "sophomore_two",
            "courses": [
                "Python",
                "Optic 2",
                "Operating System",
                "Introduction to Matlab",
                "Numerical Analysis"
            ]
        },
        {
            "name": "senior_one",
            "courses": [
                "Data Structure & Algorithm",
                "Object Orienting Programming",
                "Programming II",
                "Linear Algebra"
            ]
        },
        {
            "name": "senior_two",
            "courses": []
        },
        {
            "name": "junior_one",
            "courses": []
        },
        {
            "name": "junior_two",
            "courses": []
        }
    ]

    def __init__(self):
        '''
            Here we initialize the connection to the databse
            at init time of the database for the database instance
            to be used during this class usage.
        '''
        try:
            client = MongoClient('mongodb://localhost:27017/')
        except Exception as e:
            print("Mongo connection failed.")
            return
        # If connection succeeded check on daust_sms db
        self._db = client.daust_sms
        asyncio.run(self.create_level())


    def __repr__(self) -> str:
        return "DAUST SMS Database..."


    def students_collection(self):
        ''' Create student's collection '''
        return self._db.students


    def levels_collection(self):
        ''' Create level's collection '''
        return self._db.level


    async def create_level(self):
        ''' A student is registered to a level which represent
            the class he is in.
                - Freshman 1: freshman_one
                - Freshman 2: freshman_two
                - Sophomore 1: sophomore_one
                - Sophomore 2: sophomore_two
                - Junior 1: junior_one
                - Junior 2: junior_two
                - Senior 1: senior_one
                - Senior 2: senior_two
        '''
        self.levels_collection().insert_many(self.__levels)

    
    async def find_level(self, level):
        '''
            Return the _id of the level
        '''
        return self.levels_collection().find({ "level": level }, { "_id": 1 })


    async def create_student(self, fullname, password, email, level):
        '''
            Create a new collection of a student in the 
            daust_sms database
            A student collection must behold:
                - fullname
                - password
                - email
                - level : collection
        '''
        if level:
            level_id = await self.find_level(level)
        else:
            print("You did not specify your level.")
            return

        if fullname and password and email:
            try:
                id = self.students_collection().insert_one({
                    "fullname": fullname,
                    "password": password,
                    "email": email,
                    "level": level_id
                }).inserted_id

            except Exception as e:
                print("Could not insert {}".format(fullname))
            print("{}-[{}] has been register successfully.".format(fullname, id))
        else:
            print("Missing information")
            return


    async def update_student(self, fullname=None, email=None, level=None):
        pass
