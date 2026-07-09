from src.validators.mongo_validator import MongoValidator

queries = [

    "db.employees.find({})",

    "db.employees.find({'salary':{'$gt':70000}})",

    "db.employees.aggregate([])",

    "db.employees.deleteMany({})",

    "db.employees.drop()",

    "db.employees.updateOne({},{$set:{salary:0}})"

]

for q in queries:

    print("--------------------------------")

    print(q)

    print(MongoValidator.validate(q))