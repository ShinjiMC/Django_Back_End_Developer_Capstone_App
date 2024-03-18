# Django Back End Developer Capstone App

@ShinjiMC - By Braulio Nayap Maldonado Casilla

## Description of the Project

In this phase of the "Little Lemon" restaurant's web project, we have transitioned towards leveraging Djoser and Django REST Framework (DRF) for an enhanced API-driven approach, moving away from solely Django's traditional views. This strategic shift includes transitioning our database management from SQLite3 to MySQL, providing a more robust and scalable solution for handling data. Our primary objective in this iteration is to refine the booking and reservation system, which is crucial for both the user interface and backend operations within the restaurant's digital platform. This development is part of a comprehensive effort to cater to the varied facets of a restaurant business through a Capstone initiative, emphasizing the expansion and validation of the backend with test cases for the newly created access points, including menu, booking, and login functionalities.

## Running the Project

### Set up a Virtual Environment

To begin, install `virtualenv` if you haven't already:

```bash
pip install virtualenv
```

Create a new virtual environment:

```bash
python -m venv myenv
```

For Windows:

```bash
./myenv/Scripts/Activate.ps1
```

For Linux:

```bash
source myenv/bin/activate
```

### Installing Django and Dependencies

With the virtual environment activated, install Django, Django REST Framework, and the MySQL client for Python.

```bash
pip install django
pip install djangorestframework
pip install mysqlclient
```

If you encounter errors while trying to install mysqlclient, you can refer to the official page:
[mysqlclient on PyPI](https://pypi.org/project/mysqlclient/) For Fedora-based systems, you might need to install some dependencies:

```bash
sudo dnf install python3-devel mariadb-devel pkgconfig
```

### Setting Up MySQL

Access MySQL (MariaDB in Fedora) and set up your database and user:

```bash
sudo mysql -u root -p --socket=/var/lib/mysql/mysql.sock
```

Execute the following SQL commands to create your database and user:

```sql
create database littlelemon;
use littlelemon;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.\* TO 'django'@'localhost';
GRANT ALL PRIVILEGES ON `test_littlelemon`.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
exit;
```

### Django Project Setup

Migrate the database, create migrations for your apps, and create a superuser for the Django admin:

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
# Username: super
# Email: super@gmail.com
# Password: 123
```

### Running the Project

To start your Django development server:

```bash
python manage.py runserver
```

### Exiting the Virtual Environment

To exit the virtual environment when you're done working on the project:

```bash
deactivate
```

## Testing the API Endpoints

Ensure your development server is running and test the following endpoints with a tool like Postman or curl.

### GET Menu Item

- URL: http://localhost:8000/menu/1

_Header_:

Authorization: Token 3645695bc710ae5f9bf6a604fe9ef1f8533882b6

_Response_:

```json
{
  "id": 1,
  "title": "Greek Salad",
  "price": "12.00",
  "inventory": 100
}
```

### GET All Menu Items

- URL: http://localhost:8000/menu/

_Header_:

Authorization: Token 3645695bc710ae5f9bf6a604fe9ef1f8533882b6

_Response_:

```json
[
  {
    "id": 1,
    "title": "Greek Salad",
    "price": "12.00",
    "inventory": 100
  },
  {
    "id": 2,
    "title": "Grilled Fish",
    "price": "9.00",
    "inventory": 50
  },
  {
    "id": 3,
    "title": "Bruschetta",
    "price": "11.00",
    "inventory": 100
  },
  {
    "id": 4,
    "title": "Lemon Desert",
    "price": "7.00",
    "inventory": 50
  }
]
```

### GET Booking

- URL: http://localhost:8000/booking/tables/

_Header_:

Authorization: Token 3645695bc710ae5f9bf6a604fe9ef1f8533882b6

_Response_:

```json
[
  {
    "id": 1,
    "name": "Braulio Maldonado",
    "number_of_guests": 4,
    "booking_date": "2024-03-18T10:00:00Z"
  }
]
```

### POST Auth Login

- URL: http://localhost:8000/auth/token/login/

_Body_:

```json
{
  "password": "123",
  "username": "super"
}
```

_Response_:

```json
{
  "auth_token": "3645695bc710ae5f9bf6a604fe9ef1f8533882b6"
}
```

Use the token received in the Authorization header for subsequent requests that require authentication. Log out using http://localhost:8000/auth/token/logout/ with the token in the header.

## Running Tests

To run your Django project's tests:

```bash
python manage.py test
```

## Licencia:

Este proyecto está licenciado bajo [Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional](http://creativecommons.org/licenses/by-nc-sa/4.0/):

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
