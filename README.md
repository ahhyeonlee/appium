## 테스트 자동화 
```bash
#appium 실행 파일
appiumProject/runs.py 
```

#### Install

```bash
#djano 설치
pip install django
#bootstrap 설치
pip install django-bootstrap4
#restframework 설치
pip install djangorestframework
#cors 
pip install django-cors-headers
```

#### How to start

```bash
#mysite최상단 위치
python manage.py runserver 포트번호
```

#### How to access DB

```bash
#manage.py : 프로젝트 내 최상단 위치
python manage.py dbshell
#table list 확인(sqlite에 접근해있는 상태)
.tables
```

#### How to adjust DB

```bash
python manage.py makemigrations 
python manage.py migrate 