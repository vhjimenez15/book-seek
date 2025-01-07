# from config.mongo import mongodb
# from bson.objectid import ObjectId
# from bson.errors import InvalidId


# class BookModel:
#     def get_books_collection(self):
#         """Gets the 'books' collection."""
#         return mongodb.get_collection('books')

#     def create_book(self, data):
#         """Insert a new book."""
#         books_collection = self.get_books_collection()
#         result = books_collection.insert_one(data)
#         return str(result.inserted_id)

#     def get_all_books(self):
#         """Gets all the books."""
#         books_collection = self.get_books_collection()
#         return list(books_collection.find())

#     def get_one_book(self, book_id):
#         """Gets one book."""
#         try:
#             books_collection = self.get_books_collection()
#             return books_collection.find_one({"_id": ObjectId(book_id)})
#         except InvalidId:
#             return None

#     def update_book(self, book_id, update_data):
#         """Update a specific book."""
#         books_collection = self.get_books_collection()
#         return books_collection.update_one(
#             {"_id": ObjectId(book_id)},
#             {"$set": update_data}
#         )

#     def delete_book(self, book_id):
#         """Delete a specific book."""
#         books_collection = self.get_books_collection()
#         return books_collection.delete_one({"_id": ObjectId(book_id)})

#     def get_average_price(self, year):
#         books_collection = self.get_books_collection()
#         pipeline = [
#             {
#                 "$match": {
#                     "published_date": {
#                         "$regex": f"^{year}"
#                     }
#                 }
#             },
#             {
#                 "$group": {
#                     "_id": None,
#                     "average_price": {"$avg": "$price"}
#                 }
#             }
#         ]

#         return list(books_collection.aggregate(pipeline))
