# It's safer to define your mongomodel in a separate module
# You need to import this into your server code to use MongoDB as the database

from pymodm import MongoModel, fields


class Patient(MongoModel):  # Define the database
    # You can find commonly used fields in the class notes on the class GitHub
    name = fields.CharField()
    id = fields.IntegerField(primary_key=True)  # This will be the unique
    # identifier or the
    # primary key
    blood_type = fields.CharField()
    test_name = fields.ListField()
    test_result = fields.ListField()
