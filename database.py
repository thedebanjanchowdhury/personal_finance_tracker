import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db=client['projects']
collection = db['expenseTracker']

def insert_period(period, incomes, expenses, comment):
    return collection.insert_many([{"key": period, "incomes": incomes, "expenses": expenses, "comment": comment}])


def fetch_all_periods():
    res = collection.find()
    return res

def get_period(period):
    return collection.find_one({"key":period})

