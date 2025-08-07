from fastapi import FastAPI

app = FastAPI()

#declares path "parameters" or "variables" with the same syntax used by Python #format strings: i.e. {item_id}
#make it good practice to always give the variable its type in thie case below,
#we have put int but it will throw an error because the input_id expected is #actually a string "foo"
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}