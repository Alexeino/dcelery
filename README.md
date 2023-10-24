### Django Integration with Celery Task

*   Clone the Project dcelery
*   Go to directory celery directory
*   Create virtual environment and install requirements.txt
*   Install Redis server and start it 
```
sudo apt-get install redis-server
systemctl start redis-server
```
*   Once redis has started, start django server and celeryworker
```
./manage.py runserver
celery -A dcelery worker -l INFO
```
*   Make a post request to endpoint localhost:8000/files/upload/ and pass image file in the body.
*   Make sure to setup MailHog and change settings respectively