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

```shell
# python manage.py test <app-name> 
$ python manage.py test polls
```

## Code Coverage 확인

```shell
$ pip install coverage

# coverage run --source='.' manage.py test <app-name>
$ coverage run --source='.' manage.py test polls

$ coverage report
```

## 모델 활성화

```shell
# 모델 변경사항과 migration 변경사항을 <app-name>/migrations/ 폴더에 저장
# python manage.py makemigrations <app-name>
$ python manage.py makemigrations polls

# migration이 어떤 SQL 문장을 실행하는지 확인
$ python manage.py sqlmigrate polls 0001

# 적용되지 않은 migration들을 실행하고 자동으로 db 스키마를 관리
# 이 과정을 통해 모델에서의 변경 사항들과 데이터베이스의 스키마의 동기화가 이루어짐
$ python manage.py migrate
```
