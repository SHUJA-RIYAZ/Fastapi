from fastapi import FastAPI
from pydantic import BaseModel
 
app=FastAPI(title="mY API", version="0.1.0") #create an instance

@app.get('/')
def home():
    return {'data':{'firstname':"Shuja", 'lastname':"Riyaz"}}


@app.get('/about')
def about():
    return {'data':"This is about page"}


@app.get('/blog/{id}')
def blog(id:int):
    return {'data':id}


@app.get('/blog/{id}/comment')
def comments(id:int):
    return {'data':{'1','2'}}


@app.get('/users/me')
def read_user_me():
    return {'user_id':"the current user"}


@app.get('/users/{user_id}')
def users(user_id:str):
    return {'user_id': user_id}


@app.get("/items/{item_id}")
def read_item(item_id: int, q:str| None= None):
    return {"item_id": item_id, "q": q}


@app.get('/blog_list')
def fun_blog_list(limit:int=20,published:bool=True):
    if published :
        return f'{limit} published blog-lists'
    else:
        return f'{limit} blogs'


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},
                 {"item_name":"Shuja"},{"item_name":"SAAD"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get('/user/{userq_id}/items/{itemq_id}')
def mutiple_query(userq_id:int,itemq_id:int, q:str|None=None, short:bool=False ):
    item={"item_id":itemq_id,"owner_id":userq_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({
            "description":"This is an amazing item that has a long description"
        })
    return item

class Item(BaseModel):
    name:str
    description:str=None
    price:float
    tax:float=None
    title:str

@app.post("/items/")
def create_item(item: Item):
    return {"item":f"Blog is created with title as {item.title}" }




@app.get("/items")
def read_items(q:str|None=None):
    results={"items":[{"item_id":"FOO"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results


    