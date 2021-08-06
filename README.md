
# Restfull api (app for testing)
Welcome to Restful-app an API that you can use to learn more about API Testing or try out API testing tools against.
The API comes with projects tests on Python (coming soon JS and JAVA).
Restful-app also comes with detailed API documentation to help get you started with your API testing straight away.

### Testing app:
https://xxxx.herokuapp.com

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
Register new user

<span style="color:green">**POST**</span>
   ```buildoutcfg
    https://restfulapi.herokuapp.com/register
   ```
Example
   ```buildoutcfg
  curl -X POST
  https://restful-api.herokuapp.com/auth \
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


**Status code 400**

   ```buildoutcfg
    {'message': 'A user with that username already exists', 'uuid': 1}
   ```

Field | Type |Description
------------ | -------------| -------------
message | str | Description error
uuid | str | user uuid
