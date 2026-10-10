import shelve

with shelve.open('payments/payments') as db:
    for item in db.keys():
        print(item)
        print(db[item])
        print('_'*30)

