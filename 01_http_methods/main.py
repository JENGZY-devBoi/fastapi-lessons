from typing import Union
from fastapi import Body, FastAPI

app = FastAPI()

users = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/user')
def get_all_user():
    return users

@app.post('/user')
def create_user(user = Body()):
    user_dict = {
        'id': len(users) + 1,
        'firstname': user['firstname'],
        'lastname': user['lastname'],
        'age': user['age']
    }
    
    users.append(user_dict)
    
    return { 'message': 'Create user successfully' }

@app.get('/user/{id}')
def get_user_by_id(id: int):
    user = None
    
    for item in users:
        if id == item['id']:
            user = item
            
    if not user:
        return { 'message': 'Not found User' }
    
    return user

@app.put('/user/{id}')
def update_user_by_id(id: int, 
                      user_update = Body()):
    user = None
    user_idx = 0
    
    for idx, item in enumerate(users):
        if id == item['id']:
            user = item
            user_idx = idx
            
    if not user:
        return { 'message': 'Not found User' }
    
    users[user_idx]['firstname'] = user_update['firstname']
    users[user_idx]['lastname'] = user_update['lastname']
    users[user_idx]['age'] = user_update['age']
    
    return { 'message': 'Update User Successfuly' }
            

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}