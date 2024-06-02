from django.contrib import admin
from .models import Question
#어드민 클래스를 관리하는 부분
# Register your models here.
admin.site.register(Question)
