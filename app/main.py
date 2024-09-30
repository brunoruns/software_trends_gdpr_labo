from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

user_data = {
    "user1": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "plaintextpassword",
        "ssn": "123-45-6789"
    }
}

class User(BaseModel):
    username: str
    name: str
    email: str
    password: str
    ssn: str

@app.post('/register')
def register(user: User):
    user_data[user.username] = {
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "ssn": user.ssn
    }
    return {"message": "User registered successfully"}

@app.get('/user/{username}')
def get_user(username: str):
    if username in user_data:
        return user_data[username]
    else:
        raise HTTPException(status_code=404, detail="User not found")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
