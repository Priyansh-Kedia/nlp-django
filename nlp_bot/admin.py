from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from .models import Question
from .resources import QuestionResource


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

admin.site.register(Question, QuestionAdmin)
