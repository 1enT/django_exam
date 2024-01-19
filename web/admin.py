from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'text', 'get_choice')

	@admin.display(description="choice")
	def get_choice(self, obj):
		return Choice.objects.get(question=obj)

admin.site.register(Question, QuestionAdmin)