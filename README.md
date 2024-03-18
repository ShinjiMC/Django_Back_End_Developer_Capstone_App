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
