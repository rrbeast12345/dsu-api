li = ['apple']
import shelve
with shelve.open('logins/logins') as db:
    del db['oliver']
