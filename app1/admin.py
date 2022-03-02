from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Quiz)
admin.site.register(QuizMarks)
admin.site.register(Discussion)
admin.site.register(Reply)