# rate_limiting_service

# set up instruction

1. Install Redis and get it up and running at port 6379 (or use docker image : docker run -d -p 6379:6379 --name myredis redis)
2. clone project
3. python3 -m venv venv # create env
4. source env/bin/activate # activate env
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser --email admin@example.com --username admin # create admin user
8. python manage.py runserver # run server on localhost

# endpoint

1. use basic auth and provide username and password of admin for this curl request.

<img width="1008" alt="image" src="https://github.com/ritesshhh/rate_limiting_service/assets/25322700/5dc21d31-026c-4cd7-b834-becdf4029c59">

curl --location 'http://127.0.0.1:8000/users/' --header 'Accept: application/json; indent=4' --header 'Authorization: Basic YWRtaW46YWRtaW4='


# AB testing Results

command : ab -n 30 -c 10 -H 'Accept: application/json; indent=4' -H 'Authorization: Basic YWRtaW46YWRtaW4='  'http://127.0.0.1:8000/users/'
Rate limit selected - 10 requests/min

<img width="1273" alt="image" src="https://github.com/ritesshhh/rate_limiting_service/assets/25322700/7add5ff6-6d4b-4bbf-ab82-0adb9e4db4e8">

Results for rate limiting

<img width="454" alt="image" src="https://github.com/ritesshhh/rate_limiting_service/assets/25322700/ea41db86-7b98-4c4a-8002-2ca535de8b0d">
