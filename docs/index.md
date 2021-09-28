🇬🇧 Welcome to [Restful-app](https://stores-tests-api.herokuapp.com) an API that you can use to learn more about API Testing or try
out API testing tools. In the project repository, you can find an example of the implementation of the API tests for Python and JavaScript
(coming soon JAVA). Restful-app also comes with detailed API
[documentation](https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0)
to help get you started with your API testing straight away.

The test application simulates the operation of a store. You can create users, add an
item and pay for it.

First, learn about  sequence of entity creation
1. 👪 Create user **POST /register**
2. 🔑 Auth with data from step 1 **POST /auth**.You will get auth token
3. 📝 Add user info **POST /user_info**. This action is required to pay for the item.
4. 🏪 Add store **POST /store**
5. 🚗 Add item **POST /item** to store from step 4
6. 💵 Increase the balance for the user **POST /balance**.
7. 💳 Pay item **POST /pay**

Here you can find [examples](https://github.com/berpress/flask-restful-api/blob/main/README.md#examples-of-api-tests-in-different-languages)
 of api tests in different languages and a Docker [link](https://hub.docker.com/repository/docker/litovsky/flask_store_app)  for local use.


🇷🇺 Добро пожаловать в [Restful-app](https://stores-tests-api.herokuapp.com) API, который вы можете использовать, чтобы узнать больше о тестировании или попробовать
инструменты тестирования API. В репозитории проекта можно найти пример реализации API тестов на Python и JavaScript.
(скоро будет JAVA). Restful-app также имеет подробный API
[документацию](https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0)
чтобы помочь вам сразу приступить к тестированию API.

Тестовое приложение имитирует работу магазина. Вы можете создавать пользователей, добавлять
товар и оплачивать его.

Сначала узнайте о последовательности создания сущности.
1. 👪 Создайте пользователя **POST/зарегистрировать нового пользователя**
2. 🔑 Авторизуйтесь с данными из шага 1 **POST/auth**. Вы получите токен авторизации.
3. 📝 Добавьте информацию о пользователе **POST/user_info**. Это действие необходимо для оплаты товара.
4. 🏪 Добавьте раздел **POST/store**
5. 🚗 Добавьте товар **POST/item** для раздела, созданного в шаге 4.
6. 💵 Увеличьте баланс для пользователя **POST/balance**.
7. 💳 Оплатите товар **POST/pay**

Здесь вы можете найти [примеры](https://github.com/berpress/flask-restful-api/blob/main/README.md#examples-of-api-tests-in-different-languages)
  тестов api на разных языках и Docker [ссылка](https://hub.docker.com/repository/docker/litovsky/flask_store_app) для локального использования.
