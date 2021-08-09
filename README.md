![example workflow](https://github.com/berpress/flask-restful-api/actions/workflows/tests.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/f0089622634b09f251e9/maintainability)](https://codeclimate.com/github/berpress/flask-restful-api/maintainability)
[![.github/workflows/pytest-coverage.yml](https://github.com/berpress/flask-restful-api/actions/workflows/pytest-coverage.yml/badge.svg)](https://github.com/berpress/flask-restful-api/actions/workflows/pytest-coverage.yml)
# Restfull api (app for testing)
Welcome to Restful-app an API that you can use to learn more about API Testing or try out API testing tools against.
The API comes with projects tests on Python (coming soon JS and JAVA).
Restful-app also comes with detailed API documentation to help get you started with your API testing straight away.

### Testing app:
https://stores-tests-api.herokuapp.com

Also, you can use Docker and test this app local

### App use:
python 3.8/requests/pytest/flask

### How to start
1. Use python 3.8 +
2. Create and activate virtual environments
    ```buildoutcfg
    python3 -m venv env
   source env/bin/activate
    ```
3. Run in terminal
   ```buildoutcfg
    pip install -r requirements.txt
    ```
   or install poetry https://python-poetry.org/, then
    ```buildoutcfg
    poetry install
    ```

4. Use pre-commit hook https://pre-commit.com/#install
5. Run tests from the folder **tests** with pytest or see **Makefile**
## Commands

make +

Command | Description
------------ | -------------
lint |  Start linting
start | Start local app
tests | Run all tests

## API Documentation

First, learn about  sequence of entity creation
1. Create user **POST /register**
2. Auth with data from step 1 **POST /auth**. You will get auth token
3. Add user info **POST /user_info**. This action is required to pay for the item.
4. Add store **POST /store**
5. Add item **POST /item** to store from step 4
6. Increase the balance for the user **POST /balance**.
7. Pay item **POST /pay**


## Register
### Register user

<details>
<summary>Register new user</summary>

<span style="color:green">**POST**</span>
   ```buildoutcfg
    https://stores-tests-api.herokuapp.com/register
   ```
Example
   ```buildoutcfg
  curl -X POST
  https://stores-tests-api.herokuapp.com/register \
  -H 'Content-Type: application/json' \
  -d '{
    "username" : "admin",
    "password" : "Password11"
}'
```

**Body**

Field | Type |Description
------------ | -------------| -------------
password | str | Make a user password
username | str | Make a user username

**Response**

**Status code 200**

   ```buildoutcfg
    {'message': 'User created successfully.', 'uuid': 1}
   ```

Field | Type |Description
------------ | -------------| -------------
message | str | Success message
uuid | str | user uuid

</details>


## Authentication
### Authentication user

<details>
  <summary>Authentication user</summary>

   <span style="color:green">**POST**</span>
   ```buildoutcfg
    https://stores-tests-api.herokuapp.com/auth
   ```
Example
   ```buildoutcfg
  curl -X POST
  https://stores-tests-api.herokuapp.com/auth \
  -H 'Content-Type: application/json' \
  -d '{
    "username" : "admin",
    "password" : "Password11"
}'
```

**Body**

Field | Type |Description
------------ | -------------| -------------
password | str | User password
username | str |User username

**Response**

**Status code 200**

   ```buildoutcfg
    '{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}'
   ```

Field | Type |Description
------------ | -------------| -------------
access_token | str | Access token

</details>

## User info
### User information

<details>
  <summary>Add user information</summary>

   <span style="color:green">**POST**</span>
   ```buildoutcfg
    https://stores-tests-api.herokuapp.com/user_info/{user_id}
   ```
Example
   ```buildoutcfg
  curl -X POST
  https://stores-tests-api.herokuapp.com/user_info/1 \
  -H 'Content-Type: application/json' \
  -d '{
        "phone": "122434",
        "email": "test@test.com",
        "address": {
            "city": "Kazan",
            "street": "Limonova",
            "home_number": "11"
            },
    }'
```

**Body**

Field | Type |Description
------------ | -------------| -------------
phone | str | User phone
email | str |User email
address | Object |Address object
address/city | str | User city
address/street | str |User street
address/home_number | str |User home number



**Response**

**Status code 200**

   ```buildoutcfg
    '{"message":"User info created successfully."}'
   ```

Field | Type |Description
------------ | -------------| -------------
message | str | Result user info action

</details>

<details>
  <summary>Get user information</summary>

   <span style="color:green">**GET**</span>
   ```buildoutcfg
    https://stores-tests-api.herokuapp.com/user_info/{user_id}
   ```
Example
   ```buildoutcfg
  curl -X GET
  https://stores-tests-api.herokuapp.com/user_info/1 \
  -H 'Content-Type: application/json' \'
```



**Response**

**Status code 200**

   ```buildoutcfg
    '{'city': 'NY', 'street': 'Louge street', 'userID': 1, 'phone': '77777', 'email': 'name@test.com'}'
   ```

Field | Type |Description
------------ | -------------| -------------
city | str | User city
street | str | User street
phone | str | User phone
email | str | User email


</details>

<details>
  <summary>Delete user information</summary>

   <span style="color:green">**DELETE**</span>
   ```buildoutcfg
    https://stores-tests-api.herokuapp.com/user_info/{user_id}
   ```
Example
   ```buildoutcfg
  curl -X DELETE
  https://stores-tests-api.herokuapp.com/auth \
  -H 'Content-Type: application/json' \
```



**Response**

**Status code 200**

   ```buildoutcfg
    '{"message":"User info deleted."}'
   ```

Field | Type |Description
------------ | -------------| -------------
message | str | Result user info action

</details>

<details>
  <summary>Edit user information</summary>

   <span style="color:green">**PUT**</span>
   ```buildoutcfg
    https://stores-tests-api.herokuapp.com/user_info/{user_id}
   ```
Example
   ```buildoutcfg
  curl -X PUT
  https://stores-tests-api.herokuapp.com/auth \
  -H 'Content-Type: application/json' \
  -d '{
        "phone": "122434",
        "email": "test@test.com",
        "address": {
            "city": "Kazan",
            "street": "Limonova",
            "home_number": "11"
            },
    }'
```

**Body**

Field | Type |Description
------------ | -------------| -------------
phone | str | User phone
email | str |User email
address | Object |Address object
address/city | str | User city
address/street | str |User street
address/home_number | str |User home number



**Response**

**Status code 200**

   ```buildoutcfg
    '{'city': 'NY', 'street': 'Louge street', 'userID': 1, 'phone': '77777', 'email': 'name@test.com'}'
   ```

Field | Type |Description
------------ | -------------| -------------
city | str | User city
street | str | User street
phone | str | User phone
email | str | User email

</details>
