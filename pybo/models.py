from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') # User 모델과 1:N 관계를 가짐
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # null 허용, blank 허용
    voter = models.ManyToManyField(User, related_name='voter_question') # User 모델과 N:M 관계를 가짐

    def __str__(self):
        return self.subject

class Answer(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # null 허용
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer') # User 모델과 1:N 관계를 가짐
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # null 허용, blank 
    voter = models.ManyToManyField(User, related_name='voter_answer') 




# models.CASCADE : 연결된 객체가 삭제될 때 이를 따라가서 연결된 객체도 삭제
# models.PROTECT : 연결된 객체가 삭제되려고 할 때, ProtectedError 예외 발생
# models.SET_NULL : 연결된 객체가 삭제되면 NULL로 설정
# models.SET_DEFAULT : 연결된 객체가 삭제되면 기본 값으로 설정
# models.SET() : 연결된 객체가 삭제되면 특정 함수의 반환 값으로 설정
# models.DO_NOTHING : 아무것도 하지 않음

# ForeignKey : 다른 모델과의 연결
# on_delete : 연결된 객체가 삭제될 때 처리 방법
# related_name : 연결된 객체에서 역참조할 때 사용할 이름
# related_query_name : 쿼리에서 사용할 이름
# limit_choices_to : 선택할 수 있는 객체에 제한을 걸 때 사용
# to_field : 연결할 객체의 필드 지정
# db_constraint : 외래 키 제약 조건 생성 여부
# swappable : 모델 교체 여부
# db_index : 인덱스 생성 여부
# unique : 유일성 여부
# null : NULL 값 허용 여부
# blank : 빈 값 허용 여부
# default : 기본 값
# editable : 수정 가능 여부
# help_text : 입력 도움말
# verbose_name : 필드 이름
# verbose_name_plural : 필드 복수 이름
# validators : 유효성 검사기
# error_messages : 에러 메시지
# auto_created : 자동 생성 여부
# primary_key : 기본 키 여부
# unique_for_date : 날짜별 유일성 여부
# unique_for_month : 월별 유일성 여부
# unique_for_year : 연도별 유일성 여부
# choices : 선택지
# help_text : 입력 도움말
# db_column : 데이터베이스 컬럼 이름
# db_tablespace : 데이터베이스 테이블 스페이스
# auto_now : 자동으로 현재 시간으로 설정
# auto_now_add : 객체 생성 시 현재 시간으로 설정
# primary_key : 기본 키 여부
# unique : 유일성 여부
# db_index : 인덱스 생성 여부
# db_column : 데이터베이스 컬럼 이름
# db_tablespace : 데이터베이스 테이블 스페이스
# auto_now : 자동으로 현재 시간으로 설정
# auto_now_add : 객체 생성 시 현재 시간으로 설정
# primary_key : 기본 키 여부
# unique : 유일성 여부
# db_index : 인덱스 생성 여부
# db_column : 데이터베이스 컬럼 이름
# db_tablespace : 데이터베이스 테이블 스페이스
# auto_now : 자동으로 현재 시간으로 설정
# auto_now_add : 객체 생성 시 현재 시간으로 설정
# primary_key : 기본 키 여부
# unique : 유일성 여부
# db_index : 인덱스 생성 여부
# db_column : 데이터베이스 컬럼 이름


