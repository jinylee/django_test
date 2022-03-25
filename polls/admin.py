from django.contrib import admin

# Admin 사이트에 Model(테이블) 보이도록 등록
from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
