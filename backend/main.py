from fastapi import FastAPI, File, UploadFile, Body
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import shelve
import pickle
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()
import time
# users = {'231':["231", "Thandi Mkhize", "1976-01-01", True],'341':["341", "oliver gardi", "2008-05-23", False]}
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Mount frontend for replit
frontend_replit_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend for replit'))
print(f"Looking for frontend for replit at: {frontend_replit_path}")
print(f"Directory exists: {os.path.exists(frontend_replit_path)}")

if os.path.exists(frontend_replit_path):
    try:
        app.mount("/frontend", StaticFiles(directory=frontend_replit_path, html=True), name="frontend")
        print(f"Frontend for replit mounted at /frontend from {frontend_replit_path}")
    except Exception as e:
        print(f"Error mounting frontend for replit: {e}")
else:
    print(f"Frontend for replit not found at {frontend_replit_path}")

# Mount documentation if it exists
docusaurus_build_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../my-website/build'))
print(f"Looking for Docusaurus build at: {docusaurus_build_path}")
print(f"Directory exists: {os.path.exists(docusaurus_build_path)}")

if os.path.exists(docusaurus_build_path):
    try:
        app.mount("/documentation", StaticFiles(directory=docusaurus_build_path, html=True), name="documentation")
        print(f"Documentation mounted at /documentation from {docusaurus_build_path}")
    except Exception as e:
        print(f"Error mounting documentation: {e}")
else:
    print(f"Docusaurus build not found at {docusaurus_build_path}")


def timestamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def fixtime(t):
    return  datetime.fromtimestamp(t, tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def get_age(birthday):
    birthday = [int(x) for x in birthday.split('-')]
    now = [int(x) for x in datetime.now(timezone.utc).strftime('%Y/%m/%d').split('/')]
    years = now[0] - birthday[0]
    if now[1] == birthday[1]:
        if now[2] < birthday[2]:

            years -= 1
    elif now[1] < birthday[1]:

        years -= 1
    print(birthday)
    print(now)
    return years
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    id_number: str
    name: str
    dob: str
    password: str


class Person:
    def __init__(self, id_number, name, dob):
        self.id_number = id_number
        self.name = name
        self.dob = dob
        self.verified = False
        self.income_bracket = -1
        self.age = get_age(dob)
        self.citizenship_status = False
        self.consents = set()
        self.consent_forms = []
        self.payment = []
        self.payment_forms = []
        self.current_grants = []
        self.identifications = []
        self.grant_ids = []
        self.file_ids = []







@app.get("/")
def read_root():
    return {'success': True}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    docs_available = os.path.exists("docs")
    return {
        "status": "healthy",
        "documentation": "available" if docs_available else "not_available",
        "timestamp": timestamp()
    }

class login_info(BaseModel):
    username: str
    password: str
@app.post('/login')
def login(info:login_info):
    with shelve.open('logins/logins') as db:
        try:
            user = db[info.username]
        except:
            return {'success': False, 'bc':'abc'}
        if user[1] != info.password:
            return {'success': False, 'bc':'abc'}
        return {'success': True, 'id': user[0]}

@app.post("/test")
def tester(item: Item):
    return item
@app.post("/verify_identity")
def verify(item: Item):
    print('123')
    with shelve.open('people/people') as db:
        try:
            user = db[item.id_number]
        except:
            return {'error':'form not in database'}


    if item.name == user.name and item.dob == user.dob:

        if user.verified:
            return {'status':'verified', 'biometrics':"match"}
        else:
            return {'status': 'unverified', 'biometrics': "match"}
    else:
        return {'status': 'hidden', 'biometrics': "non-match"}
@app.post("/register")
def register(item: Item):
    with shelve.open('people/people') as db:
        if item.id_number in db.keys():
            return {'success': False}


        with shelve.open('logins/logins') as logins:
            if not item.name in logins.keys():
                logins[item.name] = [item.id_number, item.password]
            else:
                return {'success': False}
        db[item.id_number] = Person(item.id_number, item.name, item.dob)

        return {'person':db[item.id_number], 'success': True}
@app.post("/get_user")
def get(id: str):

    with shelve.open('people/people') as db:
        try:
            return db[id]
        except KeyError:
            return 'user does not exist'
@app.post("/delete user")
def delete(id: str):

    with shelve.open('people/people') as db:
        try:
            del db[id]
            return 'user removed'
        except:
            return 'user did not exist'
@app.post("/verify user")
def verify(id: str):

    with shelve.open('people/people') as db:
        try:
            if db[id].verified:
                return 'this user is already verified'
            item = db[id]
            item.verified = True
            db[id] = item
            return 'user verified'
        except:
            return 'user did not exist'
class eligibility(BaseModel):
    id_number:str
    income_bracket:int
    age:int
    citizenship_status:bool
grants = {
    'Business Grant': [3, 18, True, ['ID', 'Business Statement'], 'Apply for a business loan', '50k'],
    'Social Security': [5, 65, True, ['ID', 'Proof of Previous Employment'], 'Get Social Security benefits', '10k'],
    'Universal Income': [5, 18, True, ['Bank Statement'], 'Receive Universal Income', '300'],
    'Rent Assistance': [1, 8, -1, ['ID'], 'Apply to get assistance for rent', '700'],
    'Education Grant': [3, 18, True, ['ID', 'Grades', 'Senior Certificate'], 'Grant to help pay for college', '30k']
}


@app.post('/check_eligibility')
def check(id:str):
    with shelve.open('people/people') as db:
        try:
            user:Person = db[id]
        except:
            return {'success': False, 'user_id': id}

    approved_grants = []
    if user.income_bracket == -1 or user.age == -1:
        return {'success': False}

    for item in grants.keys():
        if user.income_bracket <= grants[item][0] and user.age >= grants[item][1] and (user.citizenship_status == grants[item][2] or grants[item][2] == -1):
            approved_grants.append({'name':item, 'requirments':', '.join(grants[item][3]), 'description':grants[item][4], 'amount':grants[item][5]})
    return {'grants':approved_grants, 'success':True}
class rec(BaseModel):
    id_number: str
    consent_given: bool
    scope: list
    remove_scope: list
@app.post('/apply')
def apply(id:str, grant:str):


    with shelve.open('people/people') as db:
        try:
            user: Person = db[id]
        except:
            return 'user does not exist'
        if grant in user.current_grants:
            return {'success': False, 'message':'you already have this grant'}

        db[user.id_number] = user
        approved_grants = {}
        if user.income_bracket == -1 or user.age == -1:

            return {'success': False, 'message':'please input your age and income on the profile tab'}
        for item in grants.keys():
            if user.income_bracket <= grants[item][0] and user.age >= grants[item][1] and (
                    user.citizenship_status == grants[item][2] or grants[item][2] == -1):
                        approved_grants[item] = grants[item][3]
        try:
            reqs = approved_grants[grant]

            for item in reqs:
                if not item in user.identifications:
                    print(user.identifications)
                    print(approved_grants)
                    print(grant)
                    return  {'success':False, 'message':"you are missing: "+', '.join(reqs)}



            with shelve.open('grants/grants') as gdb:
                ids = pickle.load(open('grants/grant.pkl', 'rb')) + 1

                pickle.dump(ids, open('grants/grant.pkl', 'wb'))

                gdb[str(ids)] = {'grant':grant, "submission date":timestamp(), 'machine_time': time.time(), 'approved':False}
            user.current_grants.append(grant)
            user.grant_ids.append(str(ids))
            db[user.id_number] = user
        except:
            return 'user is not approved for this grant'
        return {"grant": grant, "user": user, 'id': ids, 'success':True}
@app.get('/get all requirements')
def get_all_requirements():
    reqs = set()
    for value in grants.values():
        for item in value[3]:
            reqs.add(item)

    return {'requirements':reqs}
consents= ['send photos', 'see id', 'use my data to support application']

@app.get('/consent_scopes')
def consent_scopes():
    return {'scope':['Send photos', 'See ID', 'Use my data to support application']}
@app.get('/get_consent')
def get_consents(id:str):
    with shelve.open('people/people') as db:
        return {'scope':db[id].consents}

@app.post('/record_consent')
def record(form:rec):
    print(form)
    with shelve.open('people/people') as db:

        ids = pickle.load(open('consents/consents.pkl', 'rb'))+1

        pickle.dump(ids, open('consents/consents.pkl', 'wb'))
        ids = str(ids)

        try:
            user:Person = db[form.id_number]
        except:
            return 'user doesn\'t exist'

        for item in form.scope:

            user.consents.add(item)
        for item in form.remove_scope:
            try:
                user.consents.remove(item)
            except KeyError:
                pass
        user.consent_forms.append(ids)

        with shelve.open('consents/consents') as cts:
            form = form.__dict__

            form['birthday'] = timestamp()
            cts[ids] = form

        db[user.id_number] = user

    return {"form": form, "id": ids}
@app.post('/retrieve_consent_form')
def retrieve(id:str):
    with shelve.open('consents/consents') as cts:
        try:
            return cts[id]
        except:
            return 'does not exist'
class payment(BaseModel):
    id_number: str
    wallet_provider: str
    wallet_number: str
@app.post('/set_payment')
def record_pay(form:payment):
    with shelve.open('people/people') as db:

        ids = pickle.load(open('payments/payments.pkl', 'rb'))+1

        pickle.dump(ids, open('payments/payments.pkl', 'wb'))
        ids = str(ids)

        try:
            user:Person = db[form.id_number]
        except:
            return 'user doesn\'t exist'

        user.payment = [form.wallet_provider, form.wallet_number]


        user.payment_forms.append(ids)

        with shelve.open('payments/payments') as cts:
            form = form.__dict__


            form['birthday'] = timestamp()
            cts[ids] = form


        db[user.id_number] = user

    return {"form": form, "id": ids}
@app.post('/retrieve_pay_form')
def retrieve_pay(id:str):
    with shelve.open('payments/payments') as cts:
        try:
            return cts[id]
        except:
            return 'does not exist'
@app.get('/get_payment')
def get_payment(ids:str):
    with shelve.open('people/people') as db:
        try:
            return {'provider':db[ids].payment[0], 'account_number':db[ids].payment[1]}
        except:
            return {'success':False}



@app.get('/recieve_docs')
def recieve_docs(id:str):
    with shelve.open('people/people') as db:
        user = db[id]




        return {'files':user.file_ids, 'docs':user.identifications}
@app.post('/enter_identification')
def enter_identification(id:str, identification:str, image: UploadFile = File(...)):
    with shelve.open('people/people') as db:

        try:
            user = db[id]
        except:
            return {'success':False, 'message':'user does not exist'}

        if identification in user.identifications:
            return {'success':False, 'message':"this file has already been uploaded"}
        user.identifications.append(identification)
        ids = pickle.load(open('uploads/uploads.pkl', 'rb')) + 1

        pickle.dump(ids, open('uploads/uploads.pkl', 'wb'))
        ids = str(ids)
        with open(f"uploads/{ids + '.' + image.filename.split('.')[-1]}", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        user.file_ids.append(ids+'.'+image.filename.split('.')[-1])



        db[id] = user
        return {'success': True}

@app.post('/get grants')
def track_application_status(id:str):

    with shelve.open('people/people') as db:
        user = db[id]
        grants_names = []

        for grant in user.current_grants:

            ids = user.grant_ids[user.current_grants.index(grant)]


            with shelve.open('grants/grants') as gdb:
                gr = gdb[ids]

            t = 0

            while (t+gr['machine_time']) < time.time():
                t += 604800

            grants_names.append({'grant':grant, 'application_status': True, 'approved': gr['birthday'],'nextPayment':fixtime(gr['machine_time']+t),'application id':ids, 'description':grants[grant][4]})

        return {'grants':grants_names}
class user_put(BaseModel):
    name: str
    dob: str
    income_bracket: int
    age: int
    citizenship_status: bool

@app.put('/update_user')
def update_user(id:str, info:user_put):
    with shelve.open('people/people') as db:
        with shelve.open('people/people') as db:
            try:
                user: Person = db[id]
            except:
                return {'success': False}
            for attr in vars(info):
                if attr == 'dob':
                    if info.dob != user.dob:
                        get_age(info.dob)
                        user.age = get_age(info.dob)
                if not attr == 'age':
                    setattr(user, attr, getattr(info, attr))
            db[id] = user
            return {'success': True}
@app.put('/set user')
def user_set(id:str, parameter:str, value1:str):

    with shelve.open('people/people') as db:
        user = db[id]
        if value1.index(',') == -1:
            setattr(user, parameter, value1)
        else:
            setattr(user, parameter, value1.split(','))
        db[id]= user
        return {'success': True}

@app.get('/admin/get_all_applications')
def get_all_applications(password:str):
    if not password == 'admin123':
        return {'approved':False}
    users_data = []
    with shelve.open('people/people') as db:
        for user_id in db:
            user = db[user_id]
            user_info = {
                'id_number': user.id_number,
                'name': user.name,
                'dob': user.dob,
                'current_grants': []
            }
            for idx, grant in enumerate(user.current_grants):
                grant_id = user.grant_ids[idx] if idx < len(user.grant_ids) else None
                grant_details = None
                if grant_id:
                    with shelve.open('grants/grants') as gdb:
                        grant_details = gdb.get(grant_id, None)
                user_info['current_grants'].append({
                    'grant_name': grant,
                    'grant_id': grant_id,
                    'grant_details': grant_details
                })
            users_data.append(user_info)
    return {'users': users_data, 'approved':True}
@app.post('/admin/approve_grant')
def admin_approve_grant(user_id: str = Body(...), grant_id: str = Body(...)):
    with shelve.open('grants/grants', writeback=True) as gdb:
        if grant_id in gdb:
            gdb[grant_id]['approved'] = True
            return {'success': True, 'message': 'Grant approved.'}
        else:
            return {'success': False, 'message': 'Grant not found.'}

@app.post('/admin/disapprove_grant')
def admin_disapprove_grant(user_id: str = Body(...), grant_id: str = Body(...)):
    with shelve.open('people/people', writeback=True) as db:
        if user_id in db:
            user = db[user_id]
            if grant_id in user.grant_ids:
                idx = user.grant_ids.index(grant_id)
                user.grant_ids.pop(idx)
                if idx < len(user.current_grants):
                    user.current_grants.pop(idx)
                db[user_id] = user
                # Optionally, remove the grant record
                with shelve.open('grants/grants', writeback=True) as gdb:
                    if grant_id in gdb:
                        del gdb[grant_id]
                return {'success': True, 'message': 'Grant disapproved and removed.'}
            else:
                return {'success': False, 'message': 'Grant ID not found for user.'}
        else:
            return {'success': False, 'message': 'User not found.'}













