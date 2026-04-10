import pymongo
from datetime import datetime

def test_local_mongodb():
    """Test local MongoDB connection and operations"""
    try:
        # Connect to local MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print("MongoDB client created")
        
        # Test connection
        client.admin.command('ping')
        print("Local MongoDB connection successful!")
        
        # Get database
        db = client.yourtreasurer
        
        # Test collection creation and operations
        test_user = {
            "name": "test_user_local",
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
        print(f"Test user inserted with ID: {result.inserted_id}")
        
        # Find the user
        found_user = db.users.find_one({"name": "test_user_local"})
        print(f"Found user: {found_user['name']}, Budget: ${found_user['monthly_limit']}")
        
        # Update the user
        db.users.update_one(
            {"name": "test_user_local"},
            {"$set": {"current_spend": 250.0}}
        )
        print("User updated successfully")
        
        # Check update
        updated_user = db.users.find_one({"name": "test_user_local"})
        print(f"Updated spend: ${updated_user['current_spend']}")
        
        # Clean up
        db.users.delete_one({"name": "test_user_local"})
        print("Test user cleaned up")
        
        # List collections
        collections = db.list_collection_names()
        print(f"Collections: {collections}")
        
        print("Local MongoDB operations completed successfully!")
        return True
        
    except Exception as e:
        print(f"Local MongoDB connection failed: {e}")
        print("Note: Make sure MongoDB is installed and running on localhost:27017")
        return False

if __name__ == "__main__":
    test_local_mongodb()
