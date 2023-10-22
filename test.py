from fastapi import FastAPI

app = FastAPI()

# This line uses 'not' as a parameter name, causing the error
@app.get("/example")
def example(some_parameter: str):
    return {"message": "This will work!"}
