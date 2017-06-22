from django import forms
from teacher.models import Teacher
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, Field, Reset, HTML, Button
from crispy_forms.bootstrap import TabHolder, Tab, InlineCheckboxes, AppendedText, InlineRadios
from variables.models import Country, Subject_Expertise, Level_Expertise, Educational_Level, Education, Region, Education_School, Expertise_Type
# from tags.models import TagTeacher
from django.core.urlresolvers import reverse



class TeacherForm(forms.ModelForm):
    # tags = forms.CharField(label='Please add relevant skills - special needs, piano, java-programming', required=False)

    class Meta:
        model = Teacher
        fields = [

            "title",
            "first_name",
            "last_name",
            "contact",
            "birth_date",
            "gender",

            "first_subject",
            "first_level",
            "second_subject",
            "second_level",
            "third_subject",
            "third_level",

            "educational_level",
            "education",
            "education_school",
            "expertise_type",
            "years_of_experience",
            "description",
            "website_url",

            "salary_expectation",
            "salary_negotiable",
            "group_tuition",
            "region",
            "postal_code",
            "active",

            "image",
            "doc1",
            "doc1description",
            "doc2",
            "doc2description",
            "doc3",
            "doc3description",
            "doc4",
            "doc4description",
            "doc5",
            "doc5description",
            "doc6",
            "doc6description",
        ]

        labels = {
            'last_name': 'Surname',
            'contact': 'CellPhone Contact',
            'birth_date': 'Date of Birth',
            'first_level': 'Level',
            'first_subject': 'Subject',
            'second_level': 'Level',
            'second_subject': 'Subject',
            'third_level': 'Level',
            'third_subject': 'Subject',
            'educational_level': 'Your level of education',
            'education': 'Your UnderGraduate/PostGraduate courses',
            'education_school': 'Your educational institute',
            'expertise_type': 'Your current status',
            'description': 'A description of your special skills - "special needs", "piano", "java-programming"',
            'website_url': 'Your website (if any)',
            'salary_expectation': 'Your asking rate/hour',
            'postal_code': 'Your Postal Code',
            'group_tuition': 'Provide group tuitions',
            'active': 'Profile active',
            'image': 'Load your profile image',

        }

        help_texts = {
            'title': 'Please market your services - i.e reliable and results driven tutor',
            # 'active': 'Please choose active if you want your profile to be public.',
            'website_url': 'Your website and/or linkedin profile(if any)',
            # 'tags': 'Please add your specialised skills - "special needs", "nuclear-physics", "java-programming",',
        }

        widgets = {
            'birth_date': forms.SelectDateWidget(years=range(1960, datetime.date.today().year), attrs=({'style': 'width: 30%; display: inline-block;'}))
        }


    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', value='Save Details', css_class='buttonspace btn-success'))

        self.helper.layout = Layout(

            HTML("""<br><br>"""),

            Fieldset(
                'Personal details',

                Div(Field('title'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),

                Div(Field('first_name'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),

                Div(Field('last_name'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),

                Div(Field('contact'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),

                Div(Field('birth_date'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),

                Div(Field('postal_code'), css_class='col-xs-12 col-sm-4 col-md-4'),
                HTML("""<div class="row"></div>"""),

                Div(InlineRadios('gender'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),

            ),

            HTML("""<br><br>"""),

            Fieldset(
                'Your primary subject specialization',

                Div(Field('first_subject'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),
                Div(InlineCheckboxes('first_level'), css_class='col-xs-12'),

            ),

            HTML("""<br><br>"""),

            Fieldset(
                'Your secondary subject specialization',

                Div(Field('second_subject'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),
                Div(InlineCheckboxes('second_level'), css_class='col-xs-12'),
            ),

            HTML("""<br><br>"""),

            Fieldset(
                'Your other subject specialization',

                Div(Field('third_subject'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<div class="row"></div>"""),
                Div(InlineCheckboxes('third_level'), css_class='col-xs-12'),
            ),

            HTML("""<br><br>"""),

            Fieldset(
                'Educational qualifications',

                Div(InlineCheckboxes('educational_level'), css_class='col-xs-12'),

                Div(Field('education'), css_class='col-xs-12 col-sm-10 col-md-8'),

                Div(InlineCheckboxes('education_school'), css_class='col-xs-12'),

                Div(InlineRadios('expertise_type'), css_class='col-xs-12'),

                Div(Field('years_of_experience'), css_class='col-xs-4 col-sm-4 col-md-3'),

                Div(Field('description'), css_class='col-xs-12'),

                Div(Field('website_url'), css_class='col-xs-12'),

                # Div(Field('tags'), css_class='col-xs-12'),

            ),

            HTML("""<br><br>"""),

            Fieldset(
                'Other details',

                Div(Field('salary_expectation'), css_class='col-xs-6'),
                HTML("""<div class="col-xs-6 col-md-6 col-lg-6"><br></div>"""),

                Div(Field('salary_negotiable'), css_class='col-xs-6'),
                HTML("""<div class="row"></div>"""),

                Div(InlineCheckboxes('region'), css_class='col-xs-12'),

                Div(Field('group_tuition'), css_class='col-xs-12'),

                Div(Field('active'), css_class='col-xs-12'),


            ),

            HTML("""<br><br>"""),

            Fieldset(
                'Select your profile picture',
                Div(Field('image'), css_class='col-xs-12'),

            ),

            HTML("""<br>"""),

            Fieldset(
                'Loading images/documents (Requires subscription)',

                Div(Field('doc1'), css_class='col-xs-12'),
                Div(Field('doc1description'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<br>"""),
                Div(Field('doc2'), css_class='col-xs-12'),
                Div(Field('doc2description'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<br>"""),
                Div(Field('doc3'), css_class='col-xs-12'),
                Div(Field('doc3description'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<br>"""),
                Div(Field('doc4'), css_class='col-xs-12'),
                Div(Field('doc4description'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<br>"""),
                Div(Field('doc5'), css_class='col-xs-12'),
                Div(Field('doc5description'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<br>"""),
                Div(Field('doc6'), css_class='col-xs-12'),
                Div(Field('doc6description'), css_class='col-xs-12 col-sm-10 col-md-8'),
                HTML("""<br>"""),

            ),

            Fieldset(
                'Terms and conditions',
                Div(Field('termsandconditions'), css_class='col-xs-12 col-md-12'),
            )



        )


    # termsandconditions = forms.BooleanField(
    #     required=True,
    #     label="""Please check to agree that you agree to our <a href='{% url "TermsAndCondition" %}' >Terms and conditions</a>, <a href='{% url "UserAgreement" %}' >User Agreement</a> and <a href='{% url "PrivacyPolicy" %}' >Privacy Policy</a>"""
    # )

    termsandconditions = forms.BooleanField(
        required=True,
        label="""
        Please check to agree that you agree to our 
        <a href='/termsandconditions/' >Terms and conditions</a>, 
        <a href='/useragreement/' >User Agreement</a> and 
        <a href='/privacypolicy/' >Privacy Policy</a>
        """
    )


    first_level = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Level_Expertise.objects.all(),
        label="Level",
        required=True
    )

    second_level = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Level_Expertise.objects.all(),
        label="Level",
        required=False
    )

    third_level = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Level_Expertise.objects.all(),
        label="Level",
        required=False
    )

    educational_level = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Educational_Level.objects.all(),
        label="Your Level of Education"
    )

    education_school = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Education_School.objects.all(),
        label="Your Education Institute"
    )


    region = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Region.objects.all(),
        label="Your Preferred Locations"
    )


    doc1 = forms.ImageField(
        label="Load document 1",
        required=False,
    )


    doc2 = forms.ImageField(
        label="Load document 2",
        required=False,
    )

    doc3 = forms.ImageField(
        label="Load document 3",
        required=False,
    )

    doc4 = forms.ImageField(
        label="Load document 4",
        required=False,
    )

    doc5 = forms.ImageField(
        label="Load document 5",
        required=False,
    )

    doc6 = forms.ImageField(
        label="Load document 6",
        required=False,
    )


    doc1description = forms.CharField(
        label="Name document 1",
        required=False,
    )

    doc2description = forms.CharField(
        label="Name document 2",
        required=False,
    )

    doc3description = forms.CharField(
        label="Name document 3",
        required=False,
    )

    doc4description = forms.CharField(
        label="Name document 4",
        required=False,
    )

    doc5description = forms.CharField(
        label="Name document 5",
        required=False,
    )

    doc6description = forms.CharField(
        label="Name document 6",
        required=False,
    )

    # def clean_tags(self):
    #     tags = self.cleaned_data.get("tags")
    #     tags_list = tags.split(",")
    #     for i in tags_list:
    #         if not i == " ":
    #             if len(i) > 30:
    #                 raise forms.ValidationError("please make sure your tags stay below 30 characters")
    #     return tags




    def common_clean_images(self, name):

        image = self.cleaned_data.get(name, False)
        if image and getattr(self.instance, name) != image:
            if image.size > 2.0*1024*1024:
                raise forms.ValidationError("Image file too large ( > 2.0 mb )")
        return image



    def clean_image(self):
        return self.common_clean_images('image')

    def clean_doc1(self):
        return self.common_clean_images('doc1')

    def clean_doc2(self):
        return self.common_clean_images('doc2')

    def clean_doc3(self):
        return self.common_clean_images('doc3')

    def clean_doc4(self):
        return self.common_clean_images('doc4')

    def clean_doc5(self):
        return self.common_clean_images('doc5')

    def clean_doc6(self):
        return self.common_clean_images('doc6')







class SearchTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            # "region",
            # "educational_level",
            # "expertise_type",
            "group_tuition"
        ]

    def __init__(self, *args, **kwargs):
        super(SearchTeacherForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_id = 'test'
        self.helper.form_method = 'get'
        self.helper.form_id = 'search-teachers-form'
        # self.helper.form_action = reverse('Home')
        # self.helper.add_input(Submit('submit', value='Refresh', css_class='col-sm-4 col-sm-offset-1'))
        # reset = Reset('reset', 'Reset', css_class='col-sm-4 col-sm-offset-1')
        # reset = Button('reset', 'Reset', css_class='col-sm-4 col-sm-offset-1')
        # reset = Submit('reset', 'Reset', css_class='col-sm-4 col-sm-offset-1')
        # self.helper.add_input(reset)
        # self.helper.form_class = 'form-horizontal'
        # self.helper.form_class = 'search'
        self.helper.form_class = 'search'

        self.helper.layout = Layout(

            TabHolder(

                # Tab('gender',
                #     Div(InlineCheckboxes('gender'), css_class='col-xs-12 col-md-12 col-lg-12'),
                # ),
                Tab('Subject/Level',
                    # HTML("""<br>test<br>"""),
                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Subject</label></h4></div>"""),
                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Languages</b></p></span></div>"""),
                    Div(Field('subject_1'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Math & Sciences</b></p></span></div>"""),
                    Div(Field('subject_2'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Arts, Humanities & Others</b></p></span></div>"""),
                    Div(Field('subject_3'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Level</label></h4></div>"""),
                    Div(InlineRadios('level',css_class=''), css_class='col-xs-12 col-md-12 col-lg-12'),
                    ButtonHolder(
                        HTML('<a class="btn btn-default col-xs-4 col-xs-offset-4 extra-top-15" href="{% url "TeacherList" %}">Reset</a>'),
                    ),
                    ),

                Tab('Educational/Expertise',
                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Education and Expertise</label></h4></div>"""),
                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Tutors education</b></p></span></div>"""),
                    Div(InlineCheckboxes('educational_level'), css_class='col-xs-12 col-md-12 col-lg-12'),
                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Tutors current role</b></p></span></div>"""),
                    Div(InlineCheckboxes('expertise_type'), css_class='col-xs-12 col-md-12 col-lg-12'),
                    ButtonHolder(
                        HTML('<a class="btn btn-default col-xs-4 col-xs-offset-4 extra-top-15" href="{% url "TeacherList" %}">Reset</a>'),
                    ),
                    ),

                Tab('Region',

                    # Div(InlineCheckboxes('region'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><h4><label>Region</label></h4></div>"""),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>Central locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_1'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>North locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_2'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>East locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_3'), css_class='col-xs-12 col-md-12 col-lg-12'),

                    HTML("""<div class="col-xs-12 col-md-12 col-lg-12"><span><p><b>West locations</b></p></span></div>"""),
                    Div(InlineCheckboxes('region_4'), css_class='col-xs-12 col-md-12 col-lg-12'),
                    ButtonHolder(
                        HTML('<a class="btn btn-default col-xs-4 col-xs-offset-4 extra-top-15" href="{% url "TeacherList" %}">Reset</a>'),
                    ),
                    ),

                Tab('Other Details',
                    HTML("""<div class="col-xs-12 col-md-12"><h4><label>Other Details</label></h4></div>"""),
                    Div(Field('minimum_years'), css_class='col-xs-6 col-md-3'),
                    Div(Field('maximum_pay'), css_class='col-xs-6 col-md-3'),
                    
                    Div(Field('search'), css_class='col-xs-6 col-md-3'),
                    HTML("""<div class="col-xs-6 col-md-3"><b>Group Tuition</b></div>"""),
                    Div(Field('group_tuition'), css_class='col-xs-6 col-md-3'),

                    ButtonHolder(
                        Submit('submit', 'Refresh', css_class='col-xs-4 col-xs-offset-1 extra-top-15'),
                        HTML('<a class="btn btn-default col-xs-4 col-xs-offset-1 extra-top-15" href="{% url "TeacherList" %}">Reset</a>'),
                    ),
                    ),

            ),

            # ButtonHolder(
            #     Submit('submit', 'Refresh', css_class='col-xs-4 col-xs-offset-1'),
            #     HTML('<a class="btn btn-default col-xs-4 col-xs-offset-1" href="{% url "TeacherList" %}">Reset</a>'),
            # ),
        )

    subject_1 = forms.ModelChoiceField(
        # required=True,
        # widget=forms.CheckboxSelectMultiple(),
        queryset=Subject_Expertise.objects.filter(description='Languages'),
        label=""
    )
    subject_2 = forms.ModelChoiceField(
        # required=True,
        # widget=forms.CheckboxSelectMultiple(),
        queryset=Subject_Expertise.objects.filter(description='Math & Sciences'),
        label=""
    )
    subject_3 = forms.ModelChoiceField(
        # required=True,
        # widget=forms.CheckboxSelectMultiple(),
        queryset=Subject_Expertise.objects.filter(description='Arts, Humanities & Others'),
        label=""
    )


    level = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Level_Expertise.objects.all(),
        label=""
    )

    educational_level = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        queryset=Educational_Level.objects.all(),
        label=""
    )

    expertise_type = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        queryset=Expertise_Type.objects.all(),
        label=""
    )

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



    exp_choices = (
        ('1',  '1'),
        ('2',  '2'),
        ('3',  '3'),
        ('4',  '4'),
        ('5',  '5'),
        ('6',  '6'),
        ('7',  '7'),
        ('8',  '8'),
        ('9',  '9'),
        ('10',  '10'),
        ('11',  '11'),
        ('12',  '12'),
        ('13',  '13'),
        ('14',  '14'),
        ('15',  '15'),
        ('16',  '16'),
        ('17',  '17'),
        ('18',  '18'),
        ('19',  '19'),
        ('20',  '20')
    )


    minimum_years = forms.ChoiceField(
        required=False,
        initial=0,
        choices=exp_choices,
        label="Minimum Years of Experience"
    )

    # minimum_years = forms.IntegerField(
    #     required=False,
    #     initial=0,
    #     min_value=0,
    #     max_value=20,
    #     label="Minimum Years of Experience"
    # )


    pay_choices = (
        ('10',  '10'),
        ('20',  '20'),
        ('30',  '30'),
        ('40',  '40'),
        ('50',  '50'),
        ('60',  '60'),
        ('70',  '70'),
        ('80',  '80'),
        ('90',  '90'),
        ('100',  '100'),
        ('110',  '110'),
        ('120',  '120'),
        ('130',  '130'),
        ('140',  '140'),
        ('150',  '150'),
        ('160',  '160'),
        ('170',  '170'),
        ('180',  '180'),
        ('190',  '190'),
        ('200',  '200')
    )

    maximum_pay = forms.ChoiceField(
        required=False,
        initial=120,
        choices=pay_choices,
        label="Maximum Salary per hour"
    )

    # maximum_pay = forms.IntegerField(
    #     required=False,
    #     initial=120,
    #     min_value=10,
    #     max_value=300,
    #     label="Maxmium Salary per hour"
    # )

    group_tuition = forms.BooleanField(
        required=False,
        label="Group Tuition"
    )

    search = forms.CharField(
        label='Keyword Search',
        max_length=30,
        required=False
    )
