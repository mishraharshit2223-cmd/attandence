import os

from pymongo import MongoClient

from database import (
    DuplicateKeyError,
    assignments_collection,
    attendance_collection,
    hods_collection,
    initialize_database,
    students_collection,
    subjects_collection,
    teachers_collection,
)


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "attendance_db")


def migrate_collection(source_collection, target_collection, label: str) -> None:
    inserted = 0
    skipped = 0

    for item in source_collection.find({}, {"_id": 0}):
        item.pop("_id", None)
        try:
            target_collection.insert_one(item)
            inserted += 1
        except DuplicateKeyError:
            skipped += 1

    print(f"{label}: inserted={inserted}, skipped={skipped}")


def main() -> None:
    initialize_database()

    mongo_client = MongoClient(MONGO_URI)
    mongo_db = mongo_client[MONGO_DATABASE]

    migrate_collection(mongo_db["students"], students_collection, "students")
    migrate_collection(mongo_db["subjects"], subjects_collection, "subjects")
    migrate_collection(mongo_db["teachers"], teachers_collection, "teachers")
    migrate_collection(mongo_db["hods"], hods_collection, "hods")
    migrate_collection(mongo_db["assignments"], assignments_collection, "assignments")
    migrate_collection(mongo_db["attendance"], attendance_collection, "attendance")

    print("MongoDB to MySQL migration complete.")


if __name__ == "__main__":
    main()
