from django import forms

class AskForm(forms.Form):
	question = forms.CharField(label="Вопрос")

	def clean(self):
		cleaned_data = super().clean()
		if cleaned_data['question'] == 0:
			self.add_error('question', 'Поле не должно быть пустым')
		elif len(cleaned_data['question']) < 5:
			self.add_error('question', 'Минимум 5 символов')
		elif cleaned_data['question'][-1] != '?':
			self.add_error('question', 'В конце должен быть вопросительный знак')

		return cleaned_data