# Django Back End Developer Capstone App

@ShinjiMC - By Braulio Nayap Maldonado Casilla

## Description of the Project

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

### Install Django and MySQL in the Virtual Environment

Once the virtual environment is activated, install Django:

```bash
pip install django
```

pip3 install djangorestframework

And install client MySQL:

```bash
pip install mysqlclient
```

If you encounter errors while trying to install mysqlclient, you can refer to the official page:
[mysqlclient on PyPI](https://pypi.org/project/mysqlclient/)

Or use the following command for Fedora based systems:

```bash
sudo dnf install python3-devel mariadb-devel pkgconfig
```

And access to mysql with:
sudo mysql -u root -p --socket=/var/lib/mysql/mysql.sock

and execute this:

```sql
create database littlelemon;
use littlelemon;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.\* TO 'django'@'localhost';
exit;
```

```bash
python3 manage.py migrate
python3 manage.py makemigrations
python manage.py createsuperuser
#user:super
#email: super@gmail.com
#password: 123
```

### Running the Project

To run the project, execute:

```bash
python manage.py runserver
```

### Exiting the Virtual Environment

To exit the virtual environment when you're done working on the project:

```bash
deactivate
```

### TESTS

GET Menu
http://localhost:8000/menu/1

```json
{
  "id": 1,
  "title": "Greek Salad",
  "price": "12.00",
  "inventory": 100
}
```

GET Menus
http://localhost:8000/menu/

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

GET Booking
http://localhost:8000/booking/tables/

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

http://localhost:8000/auth/token/login/ to get the token
user: "super"
password: "123"

{
"auth_token": "3645695bc710ae5f9bf6a604fe9ef1f8533882b6"
}
