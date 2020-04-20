# Bill-Tacker
A python based API that helps you manage your bills and expenses. Written in Python 3.

# Installing
Clone the repository.
```
git clone https://github.com/vishrantkhanna/Bill-Tracker
```
First, you need to install Python 3.
Download it from [here](https://www.python.org/).

Install pip.
```
sudo apt-get install python3-pip
```

Install Django.
```
pip3 install django
```

Now, create the project.
```
django-admin startproject billtracker
cd billtracker/
```

Next install TastyPie, which will supply us with a REST framework.
```
pip install django-tastypie
```

Finally, start the app within the project.
```
django-admin startapp billtrackerapi
```

Setup database.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Start the server.
```
python3 manage.py runserver
```

If you get an error saying "Error: That port is already in use." Use this command:
```
sudo fuser -k 8000/tcp
```

You can access the API at (On LocalHost):
```
127.0.0.1:8000/billtracker/billtracker/
```

# Credits
[Vishrant Khanna](https://github.com/vishrantkhanna)

# License
[LICENSE.md](https://github.com/vishrantkhanna/Bill-Tracker/blob/master/LICENSE.md)
