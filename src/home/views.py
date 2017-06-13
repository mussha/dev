from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from teacher.models import Teacher
from student.models import Student
from opening.models import Opening
# from billing.models import UserCredit, ImageSubscription, FeaturedUser_0, FeaturedUser_1, AnalyticsSubscription, StudentBISubscription
# from tags.models import FavTeacher, FavOpening, ViewTeacherUnique, ViewOpening, ViewTeacherNonUnique
from home.forms import ContactForm
from django.db.models import Count
from django.conf import settings
from django.core.mail import send_mail
import datetime





class TermsAndConditionView(TemplateView):
    template_name = "termsandconditions.html"

class UserAgreementView(TemplateView):
    template_name = "privacypolicy.html"

class PrivacyPolicyView(TemplateView):
    template_name = "useragreement.html"




class PromotionView(TemplateView):
    template_name = "promotions.html"


class HomeView(TemplateView):
	template_name = "home.html"
	title = 'Your Dashboard'

	def get_context_data(self, *args, **kwargs):

		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["submit_btn_value"] = "Send"
		context["title"] = self.title
		todate = datetime.datetime.now().date()

		if self.request.user.is_authenticated():

			# todate = datetime.datetime.now()
			# todate = todate.date()
			# #delete the records beyond a certain date
			# tdelta = datetime.timedelta(days=1)
			# yesterdate = todate - tdelta

			if Teacher.objects.filter(user=self.request.user).exists():
				user = self.request.user

				#retrieve the number of credits the user has
				# usercred_obj = get_object_or_404(UserCredit, user=user)
				# usercred = usercred_obj.credit
				# context["credits"] = usercred


				# #retrieve when the user has subcription for document
				# imgsub = get_object_or_404(ImageSubscription, user=user)
				# imgsubenddate = imgsub.subenddate

				# if imgsubenddate > todate:
				# 	context["imgenddate"] = imgsubenddate
				# else:
				# 	context["imgenddate"] = "Expired"


				# #retrieve when the user has subcription for analytics
				# analsub = get_object_or_404(AnalyticsSubscription, user=user)
				# analsubenddate = analsub.subenddate

				# if analsubenddate > todate:
				# 	context["analenddate"] = analsubenddate
				# else:
				# 	context["analenddate"] = "Expired"


				# #count when does the user subcribed to advertising
				# try:
				# 	featsub = get_object_or_404(FeaturedUser_0, user=user)
				# except:
				# 	try:
				# 		featsub = get_object_or_404(FeaturedUser_1, user=user)
				# 	except:
				# 		pass

				# try:
				# 	featenddate = featsub.subenddate
				# 	if featenddate > todate:				
				# 		context["featenddate"] = featenddate
				# 	else:
				# 		context["featenddate"] = "Expired"
				# except:
				# 	context["featenddate"] = "Expired"


				user_id = Teacher.objects.filter(user=self.request.user.id).first().id
				teacher = get_object_or_404(Teacher, id=user_id)

				#list of openings favorited by you
				try:
					fav_openings = teacher.favopening_set.all()
				except Exception:
					context["fav_openings"] = 0
				else:
					context["fav_openings"] = fav_openings

				#list of student that has favorited you
				try:
					comp_fav_count = teacher.favteacher.student.all().count()
				except Exception:
					context["comp_fav_count"] = 0
				else:
					context["comp_fav_count"] = comp_fav_count

				#count of unique students who has viewed you
				try:
					comp_view_count = teacher.viewteacherunique.student.all().count()
				except Exception:
					context["comp_view_count"] = 0
				else:
					context["comp_view_count"] = comp_view_count

				#count of students that has viewed you
				try:
					nucomp_view_count = teacher.viewteachernonunique.count
				except Exception:
					context["nucomp_view_count"] = 0
				else:
					context["nucomp_view_count"] = nucomp_view_count


			elif Student.objects.filter(user=self.request.user).exists():

				user_id = Student.objects.filter(user=self.request.user.id).first().id
				studentobj = get_object_or_404(Student, id=user_id)

				user = self.request.user

				# #retrieve the number of credits the user has
				# usercred_obj = get_object_or_404(UserCredit, user=user)
				# usercred = usercred_obj.credit
				# context["credits"] = usercred


				# #retrieve when the user has subcription for BI
				# bisub = get_object_or_404(StudentBISubscription, user=user)
				# bisubenddate = bisub.subenddate
				# if bisubenddate > todate:
				# 	context["bienddate"] = bisubenddate
				# else:
				# 	context["bienddate"] = "Expired"


				#list of teacher favorited by you
				try:
					fav_teacher = studentobj.favteacher_set.all()
				except Exception:
					context["fav_teacher"] = 0
				else:
					context["fav_teacher"] = fav_teacher

			else:
				pass
				

		return context





class ContactView(FormView):
	template_name = 'forms.html'
	form_class = ContactForm
	success_url = '/'
	title = 'Contact Us'

	def form_valid(self, form):
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")				
		subject = "Site Contact Form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email] # [from_email, 'jumper23sierra@yahoo.com']
		contact_message = "Name: %s. Message: %s. Email: %s" %(form_full_name, form_message, form_email)
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=False)

		return super(ContactView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(ContactView, self).get_context_data(*args, **kwargs)
		context["submit_btn_value"] = "Send"
		context["title"] = self.title
		return context



def Test(request):
	print "test"
	return redirect("Home")


# # We need to change this so that this will work with the latest registration
# class RegisterView(FormView):
# 	template_name = 'forms.html'
# 	form_class = RegisterForm
# 	success_url = '/'
# 	title = 'Register With Us'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(RegisterView, self).get_context_data(*args, **kwargs)
# 		context["title"] = title
# 		context["submit_btn_value"] = "Register"
# 		return context

# 	def form_valid(self, form):
# 		username = form.cleaned_data['username']
# 		email = form.cleaned_data['email']
# 		password = form.cleaned_data['password2']
# 		# MyUser.objects.create_user(username=username, email=email, password=password)
# 		new_user = MyUser()
# 		new_user.username = username
# 		new_user.email = email
# 		new_user.set_password(password)
# 		new_user.save()
# 		#email user
# 		#create user profile instance
# 		#add message for succcess
# 		return redirect('Home')
# 		# return super(RegisterView, self).form_valid(form)
