import os

from pymongo import ASCENDING, MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DATABASE_NAME = "attendance_db"


client = MongoClient(MONGO_URI)
db: Database = client[DATABASE_NAME]

students_collection: Collection = db["students"]
attendance_collection: Collection = db["attendance"]
subjects_collection: Collection = db["subjects"]
teachers_collection: Collection = db["teachers"]
hods_collection: Collection = db["hods"]
assignments_collection: Collection = db["assignments"]


def initialize_database() -> None:
    """Create the indexes required for consistent attendance data."""
    teachers_collection.delete_many(
        {
            "$or": [
                {"teacher_id": None},
                {"teacher_id": {"$exists": False}},
                {"teacher_id": ""},
            ]
        }
    )
    hods_collection.delete_many(
        {
            "$or": [
                {"hod_id": None},
                {"hod_id": {"$exists": False}},
                {"hod_id": ""},
            ]
        }
    )
    subjects_collection.delete_many(
        {
            "$or": [
                {"subject_code": None},
                {"subject_code": {"$exists": False}},
                {"subject_code": ""},
            ]
        }
    )
    students_collection.create_index([("roll_no", ASCENDING)], unique=True)
    existing_indexes = attendance_collection.index_information()
    legacy_index_name = "roll_no_1_date_1"
    if legacy_index_name in existing_indexes:
        attendance_collection.drop_index(legacy_index_name)
    attendance_collection.create_index(
        [("roll_no", ASCENDING), ("date", ASCENDING), ("subject_code", ASCENDING)],
        unique=True,
    )
    subjects_collection.create_index(
        [("branch", ASCENDING), ("semester", ASCENDING), ("subject_code", ASCENDING)],
        unique=True,
    )
    teachers_collection.create_index([("teacher_id", ASCENDING)], unique=True)
    hods_collection.create_index([("hod_id", ASCENDING)], unique=True)
    hods_collection.create_index([("branch", ASCENDING)], unique=True)
    assignments_collection.create_index(
        [
            ("branch", ASCENDING),
            ("semester", ASCENDING),
            ("subject_code", ASCENDING),
            ("teacher_id", ASCENDING),
        ],
        unique=True,
    )
