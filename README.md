# software_trends_gdpr_labo

Deze file bevat alle informatie voor het oefenlabo Software Trends rond GDPR

## app in docker container

`docker build -t my-fastapi-app .`

`docker run -d -p 8000:8000 my-fastapi-app`

## Devcontainer

Run `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

## Gebruik van de API

Een gebruiker registreren:

```
curl -X POST http://localhost:8000/register \
     -H "Content-Type: application/json" \
     -d '{
           "username": "newuser",
           "name": "Jane Doe",
           "email": "jane.doe@example.com",
           "password": "securepassword",
           "ssn": "987-65-4321"
         }'

```

Gebruikerdata opvragen:

```
curl -X GET http://localhost:8000/user/newuser
```

## Java ?

`docker build -t my-springboot-app .`
`docker run -d -p 8000:8000 my-springboot-app`
