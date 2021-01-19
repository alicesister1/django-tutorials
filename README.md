# Django

## preinstallation

- pycharm community
- anaconda 3
- PostgreSQL 9.6 & pgAdmin 4.x

## Create conda environment from environment file.

```shell
conda env create -f ./mysite/environment.yml
conda activate django
```

## Run Application

```shell
cd mysite

# 장고앱 설치 및 DB 동기화
python manage.py migrate

# 0.0.0.0:8000 개발서버 실행
python manage.py runserver 0:8000
```

http://localhost:8000 또는 http://localhost:8000/admin 접속

## Test!!!

### Test back-end applications

```shell
# python manage.py test <app-name> 
python manage.py test polls
```
