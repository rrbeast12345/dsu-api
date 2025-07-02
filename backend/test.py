li = ['apple']
import shelve
with shelve.open('logins/logins') as db:
    for item in db.keys():
        print(item)
        print(db[item])
        print('___')
