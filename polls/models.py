from django.db import models


# django는 테이블을 하나의 클래스로 정의.
# django.db.models.Model 클래스를 상속받아 각 클래스 변수의 타입도 장고에서 미리 정의된 필드 클래스를 사용

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        self.choice_text
