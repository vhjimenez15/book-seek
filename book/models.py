from config.mongo import mongodb
from bson.objectid import ObjectId
from bson.errors import InvalidId


class BookModel:

    def __init__(self):
        self.collection = mongodb.get_collection('books')

    def create_book(self, data):
        """Insert a new book."""
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_all_books(self):
        """Gets all the books."""
        return list(self.collection.find())

    def get_one_book(self, book_id):
        """Get one book."""
        try:
            return self.collection.find_one({"_id": ObjectId(book_id)})
        except InvalidId:
            return None

    def update_book(self, book_id, update_data):
        """Update a specific book."""
        return self.collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": update_data}
        )

    def delete_book(self, book_id):
        """Delete a specific book."""
        return self.collection.delete_one({"_id": ObjectId(book_id)})

    def delete_many(self, data={}):
        return self.collection.delete_many(data)

    def insert_many(self, data):
        return self.collection.insert_many(data)

    def get_average_price(self, year):
        pipeline = [
            {
                "$match": {
                    "published_date": {
                        "$regex": f"^{year}"
                    }
                }
            },
            {
                "$group": {
                    "_id": None,
                    "average_price": {"$avg": "$price"}
                }
            }
        ]

        return list(self.collection.aggregate(pipeline))
