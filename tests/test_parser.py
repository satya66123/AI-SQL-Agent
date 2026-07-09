from src.parsers.mongo_parser import MongoParser

queries = [

    'db.employees.find({})',

    'db.employees.find({"department":"IT"})',

    'db.employees.find({"salary":{"$gt":70000}})',

    'db.employees.find_one({"department":"HR"})',

    'db.employees.aggregate([])'

]

for q in queries:

    print("--------------------------------")

    print(q)

    print(MongoParser.parse(q))