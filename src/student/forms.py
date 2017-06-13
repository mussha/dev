from django import forms
from student.models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, Field, Reset, HTML
from crispy_forms.bootstrap import TabHolder, Tab, InlineCheckboxes, AppendedText, InlineRadios
import datetime

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [

			"first_name",
			"last_name",
			"contact",
			"parent",
			"postal_code",
			"region",
		]

		labels = {
			'last_name': 'Surname',
			'birth_date': 'Date of Birth',
			'contact': 'CellPhone Contact',
			'parent': 'Please Tick if you are a Parent',
			'region': 'Your Location'
		}

		# help_texts = {
		# 	'contact': 'for verification purposes'
		# }

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', value='Save Details', css_class='buttonspace btn-success'))



