from django.contrib import admin
from .models import Task, Tag

# Djangoのadminサイトから操作できるモデルを設定する
admin.site.register(Task)
admin.site.register(Tag)
