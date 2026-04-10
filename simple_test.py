import pymongo
from datetime import datetime

def test_mongodb_basic():
    """Test basic MongoDB connection and operations"""
    try:
        # Try to connect with SSL disabled for testing
        client = pymongo.MongoClient(
            "mongodb+srv://priteepardeshi3011_db_user:o1UpyYozHv4zvlTn@cluster0.a5drjzn.mongodb.net/yourtreasurer?retryWrites=true&w=majority",
            tlsAllowInvalidCertificates=True,  # Allow invalid SSL certificates for testing
            serverSelectionTimeoutMS=5000
        )
        
        # Test the connection
        client.admin.command('ping')
        print("MongoDB connection successful!")
        
        # Get database
        db = client.yourtreasurer
        
        # Test collection creation and operations
        test_user = {
            "name": "test_user_basic",
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
        found_user = db.users.find_one({"name": "test_user_basic"})
        print(f"Found user: {found_user['name']}, Budget: ${found_user['monthly_limit']}")
        
        # Update the user
        db.users.update_one(
            {"name": "test_user_basic"},
            {"$set": {"current_spend": 250.0}}
        )
        print("User updated successfully")
        
        # Check update
        updated_user = db.users.find_one({"name": "test_user_basic"})
        print(f"Updated spend: ${updated_user['current_spend']}")
        
        # Clean up
        db.users.delete_one({"name": "test_user_basic"})
        print("Test user cleaned up")
        
        # List collections
        collections = db.list_collection_names()
        print(f"Collections: {collections}")
        
        print("MongoDB operations completed successfully!")
        return True
        
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    test_mongodb_basic()
