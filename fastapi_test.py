#FastAPI is a class inherting from starlette and Starlette is a lightweight,#ASGI framework/toolkit for building async web services in python
#fastapi is built on top of starlette meaning it uses starlettes core features #nd adds more on top
#starlette provides: routing, middleware, request/response handliing, #ackground tasks, websockets, static file serving. (does the heavy lifting)
#then fastapi takes all that starlette provides and adds : automatic OpenAI #ocs, data validationn with pydantic, dependnecy injection and type hints for #equest bodies
#its like startlette os the car engine then fastpi is the full car with dashboard, gps and carseats
#wsgi(web server gateway interface) - is synchronous, older using django/flask, #ts concurrency: one request at a time per worker, doesn"t support websockets #r background task : in simple terms its like a single lane highway: each #equest waits its turn and struggles with real time features like notifications
#asgi(asynchronous server gateway interface):  is syncrounous and #ynchrounous, #websockkets and native support for background tasks.
#concurrency refers to multiple tasks in progress
#websockets are a persistent , two way connections between client and server    #and allow real time connection
from fastapi import FastAPI
#creat a FastAPI isntance wherbey the variable app is the instance of the class fastapi and is the main point of intercation to create all apis
app = FastAPI()

#we have the path i.e. / also called an endpoint or route whereas get is an #peration just as post/get/put/delete/options/head/patch/trace is and the @ is # decorater which takes the function below and executes it
@app.get("/")

#the below is an asynchronous function named root. note that it uses #non-blocking input and output, can pause while waiting for other tasks to run #and must be called with await which is different from the def get_data function #commented below which runs one step at a time , blocks the program while it #waiits and doesnt use await
async def root():
    return {"message": "Hello World"}

#def get_data():
#  response = requests.get("https://api.example.com/data")
#   return response.json()

#note to run this file we use : fastapi dev fastapi_test.py
#copy the url to a browser of your choice
#itshows the jason response i.e. {"message": "Hello world"}
#fastAPI creates a schema 
#a schema is the definition of sth not code
# an api schema in this case OpenAPI is a specification dictating how to define #a schema of your API
#data schema is the shape of data like json content
# add the extension/docs to see the swagger ui and intercat with it