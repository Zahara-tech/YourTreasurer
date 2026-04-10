from flask_pymongo import PyMongo
from flask import Flask
from datetime import datetime
import pymongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://priteepardeshi3011_db_user:o1UpyYozHv4zvlTn@cluster0.a5drjzn.mongodb.net/yourtreasurer"

try:
    mongo = PyMongo(app)
    print("✅ Flask-PyMongo initialized successfully")
except Exception as e:
    print(f"❌ Flask-PyMongo initialization failed: {e}")
    # Try direct pymongo connection
    try:
        client = pymongo.MongoClient("mongodb+srv://priteepardeshi3011_db_user:o1UpyYozHv4zvlTn@cluster0.a5drjzn.mongodb.net/")
        db = client.get_database()
        print("✅ Direct PyMongo connection successful")
        mongo = type('MockMongo', (), {'db': db})()
    except Exception as e2:
        print(f"❌ Direct PyMongo connection also failed: {e2}")
        exit(1)

def test_mongodb_connection():
    try:
        # Test basic connection
        print("Testing MongoDB connection...")
        
        # Test creating a collection by inserting a test user
        test_user = {
            "name": "test_user",
            "password": "test123",
            "monthly_limit": 1000.0,
            "current_spend": 0,
            "start_date": datetime.now(),
            "created_at": datetime.now(),
            "email_sent_10": False,
            "email_sent_5": False,
            "email_sent_0": False
        }
        
        # Insert test user (this will create the 'users' collection automatically)
        result = mongo.db.users.insert_one(test_user)
        print(f"✅ Test user inserted with ID: {result.inserted_id}")
        
        # Test reading the user back
        found_user = mongo.db.users.find_one({"name": "test_user"})
        if found_user:
            print(f"✅ Test user found: {found_user['name']}, Budget: ${found_user['monthly_limit']}")
        else:
            print("❌ Test user not found")
        
        # Test updating the user
        mongo.db.users.update_one(
            {"name": "test_user"},
            {"$set": {"current_spend": 150.0}}
        )
        print("✅ Test user updated")
        
        # Test reading updated user
        updated_user = mongo.db.users.find_one({"name": "test_user"})
        print(f"✅ Updated user spend: ${updated_user['current_spend']}")
        
        # Clean up - remove test user
        mongo.db.users.delete_one({"name": "test_user"})
        print("✅ Test user cleaned up")
        
        # List all collections
        collections = mongo.db.list_collection_names()
        print(f"✅ Available collections: {collections}")
        
        print("\n🎉 MongoDB connection and CRUD operations working perfectly!")
        return True
        
    except Exception as e:
        print(f"❌ MongoDB Error: {e}")
        return False

if __name__ == "__main__":
    test_mongodb_connection()
