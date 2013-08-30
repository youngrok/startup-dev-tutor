# Django로 웹사이트 만들고 런칭하기

프로그래밍을 처음 해보는 사람이 Python 언어와 Django 프레임웍, 그외에 기타 여러 도구를 활용해서 기본적인 기능을 갖춘 웹사이트를 개발하고 런칭해본다.

## 개발할 웹사이트의 내용
미니 쇼핑몰. Django Admin을 통해서 쇼핑몰 컨텐츠를 등록하면, 웹페이지에서 컨텐츠를 전시하고, 사용자가 구매하고, 댓글을 달 수 있게 한다.

### 기능 목록
* 회원가입 / 로그인
* 상품 목록 보기
* 상품 상세 내역 보기
* 구매하기
* 구매내역 보기
* 댓글

### 학습하게 되는 기술
* HTML / CSS 기초
* Python 기초
* Django 사용법
* Bootstrap 활용
* MVC 개념
* 버전 관리

## 개발 환경 준비
### 개발 도구
* [Sublime Text](http://www.sublimetext.com/)
* [Firefox](http://www.mozilla.org/ko/firefox/new/)
* [Homebrew](http://brew.sh/)
* [GitX](http://gitx.laullon.com/)

### Python & Django

    brew install python
	pip install ipython
	pip install django
    

* Django bash completion

## Django로 웹사이트 개발
### 프로젝트 만들기
    mkdir workspace
    cd workspace
    django-admin.py startproject minishop
    cd minishop
    chmod +x manage.py
    ./manage.py startapp shopping
    ./manage.py runserver
    
[http://localhost:8000](http://www.mozilla.org/ko/firefox/new/) 접속

### git 저장소에 보관	
* [github](http://github.com) 가입, 저장소 만들기
* gitx로 커밋
* github에 push
	
### Hello World
1. urls.py에 url 등록
1. settings.py에 app 등록
1. 텍스트로 Hello World!! 출력
1. html로 출력

### HTML 기초
* h1~h6
* a
* p
* div
* table
* ul, ol, li

### CSS 기초
* font, color
* inline/block element
* content flows, float
* box model
* css file, style tag
* Bootstrap

### The Fancy UI 따라하기
* navbar
* 상품 사진
* 상품 이름
* grid 배열

### 상품 실제 데이터로 입력
* sqlite3
* model 설계
* django shell에서 갖고 놀기
* 파이썬 기초 문법
* django admin에서 데이터 입력 

### 상품 상세화면
* 링크 누르면 상세화면으로 이동
* 상품 사진, 이름, 설명
* 구매 버튼

### 로그인
* 로그인이 필요한 기능 처리
* 로그인 페이지
* 가입
* 로그아웃

### 구매
* 구매 처리
* 구매 목록 보여주기

### 댓글
* 댓글 입력 UI
* 댓글 저장
* 댓글 보여주기

## Deployment
### Heroku

