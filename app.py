
# Import statements
import asyncio
from helpers.db import MongoManager

# This is the main file where all codes will be called

if __name__ == "__main__":

    mg = MongoManager()
    asyncio.run(
        mg.new_student("Jonathan Ndao", "Pass@123/",
                       "jndao@example.com", "Junior")
    )
