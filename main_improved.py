from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
import os

app = FastAPI()

# Genereer een sleutel voor encryptie
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Sensitieve data wordt versleuteld
user_data = {
    "user1": {
        "name": cipher_suite.encrypt(b"John Doe"),
        "email": cipher_suite.encrypt(b"john.doe@example.com"),
        "password": generate_password_hash("plaintextpassword"),
        "ssn": cipher_suite.encrypt(b"123-45-6789")
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
        "name": cipher_suite.encrypt(user.name.encode()),
        "email": cipher_suite.encrypt(user.email.encode()),
        "password": generate_password_hash(user.password),
        "ssn": cipher_suite.encrypt(user.ssn.encode())
    }
    return {"message": "User registered successfully"}

@app.get('/user/{username}')
def get_user(username: str):
    if username in user_data:
        user = user_data[username]
        decrypted_user = {
            "name": cipher_suite.decrypt(user['name']).decode(),
            "email": cipher_suite.decrypt(user['email']).decode(),
            "ssn": cipher_suite.decrypt(user['ssn']).decode()
        }
        return decrypted_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

if __name__ == '__main__':
    import uvicorn
    # Gebruik HTTPS in productie
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")



""" Encryptie:

    De cryptography.fernet bibliotheek wordt gebruikt voor het versleutelen van sensitieve gegevens.
    De werkzeug.security bibliotheek wordt gebruikt voor het hashen van wachtwoorden.

    

Gebruik van HTTPS:

    De app wordt gestart met SSL-context om HTTPS te gebruiken. Dit vereist een SSL-certificaat (cert.pem) en een sleutel (key.pem).
    Die kun je enkel lokaal testen door de tag --insecure toe te voegen aan een curl call:

    curl -X POST https://localhost:5000/register \
     -H "Content-Type: application/json" \
     -d '{
           "username": "newuser",
           "name": "Jane Doe",
           "email": "jane.doe@example.com",
           "password": "securepassword",
           "ssn": "987-65-4321"
         }' \
     --insecure
     
     curl -X GET https://localhost:5000/user/newuser --insecure


Consent moet open zijn en granulair:

    Dit is niet direct in de code weergegeven, maar in een echte toepassing zou je een mechanisme moeten implementeren waarmee gebruikers expliciet toestemming kunnen geven voor het verzamelen en gebruiken van hun gegevens. Dit kan bijvoorbeeld worden gedaan via een registratieformulier waarin de gebruiker kan aangeven welke gegevens ze willen delen.



 """