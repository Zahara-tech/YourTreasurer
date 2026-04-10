import pymongo
from datetime import datetime
import urllib.parse

def test_user_mongodb():
    """Test user's MongoDB Atlas connection and operations"""
    try:
        # Connect to user's MongoDB Atlas with proper encoding
        print("Connecting to MongoDB Atlas...")
        encoded_password = urllib.parse.quote_plus("Zahara@#$1")
        client = pymongo.MongoClient(
            f"mongodb+srv://Zahara:{encoded_password}@cluster0.dyxzgxe.mongodb.net/yourtreasurer?retryWrites=true&w=majority",
            serverSelectionTimeoutMS=10000
        )
        
        # Test connection
        client.admin.command('ping')
        print("✅ MongoDB Atlas connection successful!")
        
        # Get database
        db = client.yourtreasurer
        
        # Test collection creation and operations
        test_user = {
            "name": "test_user_atlas",
            "password": "test123",
            "monthly_limit": 1000.0,
            "current_spend": 0,
            "start_date": datetime.now(),
            "created_at": datetime.now(),
            "email_sent_10": False,
            "email_sent_5": False,
            "email_sent_0": False
        }
        
        # Insert test user
        result = db.users.insert_one(test_user)
        print(f"✅ Test user inserted with ID: {result.inserted_id}")
        
        # Find the user
        found_user = db.users.find_one({"name": "test_user_atlas"})
        print(f"✅ Found user: {found_user['name']}, Budget: ${found_user['monthly_limit']}")
        
        # Update the user
        db.users.update_one(
            {"name": "test_user_atlas"},
            {"$set": {"current_spend": 250.0}}
        )
        print("✅ User updated successfully")
        
        # Check update
        updated_user = db.users.find_one({"name": "test_user_atlas"})
        print(f"✅ Updated spend: ${updated_user['current_spend']}")
        
        # Clean up
        db.users.delete_one({"name": "test_user_atlas"})
        print("✅ Test user cleaned up")
        
        # List collections
        collections = db.list_collection_names()
        print(f"✅ Collections: {collections}")
        
        print("\n🎉 MongoDB Atlas operations completed successfully!")
        print("All data is being stored in MongoDB Atlas!")
        return True
        
    except Exception as e:
        print(f"❌ MongoDB Atlas connection failed: {e}")
        return False

if __name__ == "__main__":
    test_user_mongodb()
