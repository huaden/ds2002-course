#!/Users/haydenrobinette/miniforge3/envs/ds2002/bin/python3
from pymongo import MongoClient, errors
import os

# Use environment variables from README: MONGODB_ATLAS_URL, MONGODB_ATLAS_USER, MONGODB_ATLAS_PWD
uri = os.getenv('MONGODB_ATLAS_URL')
username = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PWD')

# Connect to the MongoDB Atlas cluster
client = MongoClient(uri, username=username, password=password, connectTimeoutMS=200, retryWrites=True)

def main():
    db = client.bookstore
    
    totalAuthors = db.authors.count_documents({})
    print(f"Total Authors: {totalAuthors}")
    print("-" * 15)
    
    for author in db.authors.find().sort("name", 1):
        print(f"Name: {author.get('name')}")
        print(f"Nationality: {author.get('nationality')}")
        print(f"Birthday: {author.get('birthday')}")
        print(f"Bio: {author.get('bio').get('short')}")

        print("-" * 15)

    client.close()

if __name__ == "__main__":
    main()