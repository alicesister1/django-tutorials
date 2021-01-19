# Django

## preinstallation

- pycharm community
- anaconda 3
- PostgreSQL 9.6 & pgAdmin 4.x

## Create conda environment from environment file.

```shell
$ conda env create -f ./mysite/environment.yml
$ conda activate django
```

## Run Application

```shell
$ cd mysite

# 장고앱 설치 및 DB 동기화
$ python manage.py migrate

# 0.0.0.0:8000 개발서버 실행
$ python manage.py runserver 0:8000
```

http://localhost:8000 또는 http://localhost:8000/admin 접속

## Test!!!

### Test back-end applications

```shell
# python manage.py test <app-name> 
$ python manage.py test polls
```

## Test client-side

> 장고는 뷰 레벨에서 코드와 상호 작용하는 사용자를 시뮬레이션 하기 위한 테스트 클래스 Client 제공

```shell
$ python manage.py shell
```

```shell
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> client = Client()
>>> response = client.get('/')
>>> response.status_code
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
>>> response.content
>>> response.context['latest_question_list']
```