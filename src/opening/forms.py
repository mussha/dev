from django import forms
from teacher.models import Teacher
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, Field, Reset, HTML
from crispy_forms.bootstrap import TabHolder, Tab, InlineCheckboxes, AppendedText, InlineRadios
from opening.models import Opening
from variables.models import Level_Expertise, Region, Subject_Expertise, Educational_Level, Expertise_Type




price_choices = (
	('20', '20'),
	('25', '25'),
	('30', '30'),
	('35', '35'),
	('40', '40'),
	('45', '45'),
	('50', '50'),
	('55', '55'),
	('60', '60'),
	('65', '65'),
	('70', '70'),
	('75', '75'),
	('80', '80'),
	('85', '85'),
	('90', '90'),
	('95', '95'),
	('100', '100'),
	('105', '105'),
	('110', '110'),
	('115', '115'),	
	('120', '120'),	
	('125', '125'),	
	('130', '130'),	
	('135', '135'),
	('140', '140'),
	('145', '145'),
	('150', '150'),
	('155', '155'),
	('160', '160'),
	('165', '165'),
	('170', '170'),
	('175', '175'),
	('180', '180'),
	('185', '185'),
	('190', '190'),
	('195', '195'),
	('200', '200'),

)





class PriceForm(forms.Form):
    price = forms.ChoiceField(label='Your offer - $/hr ', choices=price_choices )


class OpeningForm(forms.ModelForm):

	class Meta:
		model = Opening
		fields = [

			"title",
			"subject",
			"level",
			"description",
			"salary_range",
			"negotiable",
			"region",
			# "private",
			"group_tuition",
			# "job_active"
			

		]

		labels = {
			'salary_range': 'Your offering rate/hour',
			'negotiable': 'Negotiable offering rate',
			'description': 'Please state other requirements',
			'region': 'Your region',
			# 'private': 'Hide this job from public',
			'group_tuition': 'Group tuition',
		}

		help_texts = {
			'title': 'Please state what you are looking for, i.e Looking for a results driven math tutor',
			# 'job_active': 'Please choose active to activate this opening.',
			# 'negotiable': 'Is the salary negotiable.',
		}


	def __init__(self, *args, **kwargs):
		super(OpeningForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', value='Save Details', css_class='buttonspace btn-success'))

		self.helper.layout = Layout(

            HTML("""<br><br>"""),

            Fieldset(
            	'Job Details',

            	Div(Field('title'), css_class='col-xs-12 col-sm-10 col-md-8'),
            	HTML("""<div class="row"></div>"""),

				Div(Field('subject'), css_class='col-xs-12 col-sm-10 col-md-8'),
				HTML("""<div class="row"></div>"""),

				Div(InlineRadios('level'), css_class='col-xs-12'),

				HTML("""<div class="col-sm-12"><br></div>"""),

				Div(Field('description'), css_class='col-xs-12'),

            ),

            HTML("""<br>"""),

            Fieldset(
            	'Other Details',

				Div(Field('salary_range'), css_class='col-xs-6'),
				HTML("""<div class="col-xs-6 col-md-6 col-lg-6"><br></div>"""),

				Div(Field('negotiable'), css_class='col-xs-6'),
				HTML("""<div class="row"></div>"""),

				Div(InlineRadios('region'), css_class='col-xs-12'),
				HTML("""<div class="row"></div>"""),

				Div(Field('group_tuition'), css_class='col-xs-12'),

				# HTML("""<div class="row"></div>"""),

				# Div(Field('job_active'), css_class='col-xs-12'),
            ),

		)




level_grp = (
	('Lower Primary', 'Lower Primary'),
	('Higher Primary', 'Higher Primary'),
	('Lower Secondary', 'Lower Secondary'),
	('Higher Secondary', 'Higher Secondary'),
	('Junior College', 'Junior College'),
	('University', 'University')
)

class SearchOpeningForm(forms.ModelForm):

	class Meta:
		model = Opening
		fields = [

				# "subject",
				# "level",
				# "region",

		]

	def __init__(self, *args, **kwargs):
		super(SearchOpeningForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		# self.helper.form_id = 'test'
		self.helper.form_method = 'get'
		# self.helper.form_action = reverse('Home')
		# self.helper.add_input(Submit('submit', value='Refresh', css_class='btn-block btn-success'))
		# self.helper.add_input(Reset('name', 'Reset')) #implement this when jquery is up and remove submit
		# self.helper.form_class = 'form-horizontal'
		# self.helper.form_class = 'search'

		self.helper.layout = Layout(

			TabHolder(

				Tab('Subject/Level',

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Select Subject</label></h4></div>"""),
                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Languages</b></p></span></div>"""),
                    Div(InlineRadios('subject_1'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Math & Sciences</b></p></span></div>"""),
                    Div(InlineRadios('subject_2'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Arts, Humanities & Others</b></p></span></div>"""),
                    Div(InlineRadios('subject_3'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Select Level</label></h4></div>"""),
                    Div(InlineRadios('level_grp'), css_class='col-xs-12 col-md-12 col-lg-12'),

					# Div(InlineRadios('subject'), css_class='col-xs-12 col-md-12 col-lg-12'),
					# Div(InlineRadios('level'), css_class='col-xs-12 col-md-12 col-lg-12'),
				),
				Tab('Your Preferred Regions',

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Region</label></h4></div>"""),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Central locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_1'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>North locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_2'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>East locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_3'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>West locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_4'), css_class='col-xs-12 col-md-12 col-lg-12'),

					# Div(InlineCheckboxes('region'), css_class='col-xs-12 col-md-12 col-lg-12'),
				),
				# Tab('Salary',
				# 	Div(Field('minimum_pay'), css_class='col-xs-12 col-md-3 col-lg-3'),
				# ),
				# Tab('Keyword Description Search',
				# 	Div(Field('search'), css_class='col-xs-12 col-md-6 col-lg-6'),
				# ),

                Tab('Other Details',
                	HTML("""<div class="col-xs-12 col-md-12"><h4><label>Other Details</label></h4></div>"""),

                	Div(Field('minimum_pay'), css_class='col-xs-6 col-md-4'),
					Div(Field('search'), css_class='col-xs-6 col-md-4'),

                    # Div(Field('minimum_years'), css_class='col-xs-12 col-md-6 col-lg-6'),
                    # Div(Field('maximum_pay'), css_class='col-xs-12 col-md-6 col-lg-6'),
                    
                    # Div(Field('search'), css_class='col-xs-12 col-md-6 col-lg-6'),
                    # HTML("""<div class="col-xs-6 col-md-4"><br></div>"""),
                    Div(Field('group_tuition'), css_class='col-xs-6 col-md-4'),
                    
                    ),


			),

            ButtonHolder(
                Submit('submit', 'Refresh', css_class='col-xs-4 col-xs-offset-1'),
                HTML('<a class="btn btn-default col-xs-4 col-xs-offset-1" href="{% url "OpeningList" %}">Reset</a>'),
            ),


		)



	subject_1 = forms.ModelMultipleChoiceField(
		required=True,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Subject_Expertise.objects.filter(description='Languages'),
		label=""
	)
	subject_2 = forms.ModelMultipleChoiceField(
		required=True,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Subject_Expertise.objects.filter(description='Math & Sciences'),
		label=""
	)
	subject_3 = forms.ModelMultipleChoiceField(
		required=True,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Subject_Expertise.objects.filter(description='Arts, Humanities & Others'),
		label=""
	)



	level_grp = forms.ChoiceField(
		label='Level', 
		choices=level_grp )


	region_1 = forms.ModelMultipleChoiceField(
		required=False,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Region.objects.filter(description='Central'),
		label=""
	)

	region_2 = forms.ModelMultipleChoiceField(
		required=False,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Region.objects.filter(description='North'),
		label=""
	)

	region_3 = forms.ModelMultipleChoiceField(
		required=False,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Region.objects.filter(description='East'),
		label=""
	)

	region_4 = forms.ModelMultipleChoiceField(
		required=False,
		widget=forms.CheckboxSelectMultiple(),
		queryset=Region.objects.filter(description='West'),
		label=""
	)


	minimum_pay = forms.IntegerField(
		required = False,
		initial = 20,
		min_value = 10,
		max_value = 300,
		label="Minimum Salary per hour"
		)

	group_tuition = forms.BooleanField(
		required=False,
		label="Group Tuition"
	)

	search = forms.CharField(
		label='Search for Keywords', 
		max_length=30,
		required = False
	)