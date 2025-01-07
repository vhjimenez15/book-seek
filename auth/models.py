from datetime import datetime
from bson.objectid import ObjectId
from config.mongo import mongodb


class UserModel:
    def __init__(self):
        self.collection = mongodb.get_collection("users")

    def create_user(self, username, password, **extra_fields):
        """Insert a new user."""
        user = {
            "username": username,
            "password": password,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            **extra_fields
        }
        result = self.collection.insert_one(user)
        return str(result.inserted_id)

    def get_all_users(self):
        """Gets all users."""
        return self.collection.find()

    def get_one_user(self, user_id):
        """Get one user."""
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def update_user(self, user_id, update_data):
        """Update a specific user."""
        update_data["updated_at"] = datetime.utcnow()
        result = self.collection.update_one(
            {"_id": user_id}, {"$set": update_data}
        )
        return result.modified_count

    def delete_user(self, user_id):
        """Delete a specific user."""
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count

    def delete_many(self, data={}):
        return self.collection.delete_many(data)

    def authenticate_user(self, username, password):
        """Authenticate user."""
        user = self.collection.find_one(
            {"username": username, "password": password}
        )
        return user if user else None

    def get_user_by_username(self, username):
        return self.collection.find_one({"username": username})

    def get_user_by_id(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})
