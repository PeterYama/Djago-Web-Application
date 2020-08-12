# Django & Django Rest Framework Example


**This Django application includes:**
  - Apps and routes
  - Databases and models 
  - Foreign key constraint
  - Styling the page with CSS
  - Testing Scripts
  - HttpResponse
  - Custom Admin pages and more


This application was made following [Django Documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
, User can select options from a question that are saved in the database
### Added a simple css styling
![Styling](https://i.imgur.com/ezh2k1b.jpg)


Choices are related to questions using foreing keys    |  Choices are saved to the database and shown to the user
:-------------------------:|:-------------------------:
![Question Template](https://i.imgur.com/97CXreS.jpg)  |  ![Choices](https://i.imgur.com/635bqvM.jpg)


**Django Rest Framework application includes:**
  - DRF framework structure
  - View Sets 
  - CRUD 
  - Requests with HTTPie
  - Routers

## Example 
### Get all clients with HTTPie:
```
  http http://127.0.0.1:8000/clients/
```

```json
  [
    {
        "address": "First Street",
        "age": 24,
        "id": 1,
        "name": "Mario Silva"
    },
    {
        "address": "Second Street",
        "age": 24,
        "id": 3,
        "name": "Maria"
    },
    {
        "address": "Second Street",
        "age": 24,
        "id": 4,
        "name": "Maria"
    }
]
```
### Get a specific client
```
http http://127.0.0.1:8000/clients/1/
```
```jason
{
    "address": "First Street",
    "age": 24,
    "id": 1,
    "name": "Mario Silva"
}
```
### Update an specific Client
```
http POST http://127.0.0.1:8000/clients/1/
```
#### Body of the request updating the address:
```jason
{
    "address": "Smith Street",
    "age": 24,
    "id": 1,
    "name": "Mario Silva"
}
```
#### Response
```jason
{
    "address": "Smith Street",
    "age": 24,
    "id": 1,
    "name": "Mario Silva"
}
```
### Delete a specific client
```
http DELETE http://127.0.0.1:8000/clients/1/
```
