from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.views.generic import TemplateView, View, FormView
# from tags.models import ViewTeacherRecord, SearchWordTeacherRecord
# from orders.models import Order

from home.forms import OrderChartForm
from django.contrib.auth.models import User
from datetime import date
import datetime
import json
import pandas as pd
from django.db.models import Q




def json_serial(obj):
	"""JSON serializer for objects not serializable by default json code"""
	if isinstance(obj, date):
		serial = obj.isoformat()
		return serial
	raise TypeError ("Type not serializable")




class TeacherChart(View):

	def get(self, request):
		template = 'tcharts.html'

		enddate = datetime.datetime.now()
		tdelta = datetime.timedelta(days=30)
		startdate = enddate - tdelta
		startdate = startdate.date()

		#filtering all the search keywords for the start and enddate
		swdf = SearchWordTeacherRecord.objects.filter(date__range=[startdate, enddate])

		try:
			swdf = swdf.values_list('id','word','user','subject','date', flat=False)
			#inserting the collected data into a dateframe for manipulation
			swdf = pd.DataFrame(list(swdf))
			#giving the dataframe column names
			swdf.columns = ['id','word','user','subject','date']
			#do a groupby
			swdf = swdf.groupby(['word'], as_index=False)['user'].count()
			#selecting the required columns
			swdf = swdf[['word','user']]
			#sorting the values
			swdf.sort_values('user', ascending=True, inplace=True)
			#changing column names from user to users
			swdf.rename(columns={'user':'users'}, inplace=True)
			#only taking in the top 20 searches
			swdf = swdf.head(20)
			#adding the header to a list format
			swdfcolumn = [swdf.columns.values.tolist()]
			#adding the values to a list format
			swdf = swdf.values.tolist()
			#adding both together
			swdf = swdfcolumn + swdf

		except:
			dnotexist = "Data does not exist yet"



		#filtering for the correct teacher
		df = ViewTeacherRecord.objects.filter(teacher=self.request.user.teacher)


		try:

			df = df.values_list('id','teacher_id','uniquecount','nonuniquecount','msgcount','ordercount','date','updated','timestamp', flat=False)
			#inserting the collected data into a dateframe for manipulation
			df = pd.DataFrame(list(df))
			#giving the dataframe column names
			df.columns = ['id','teacher_id','uniquecount','nonuniquecount','msgcount','ordercount','date','updated','timestamp']
			#rename required columns
			df.rename(columns={'uniquecount':'Unique Views','nonuniquecount':'Views','msgcount':'Messages','ordercount':'Orders'}, inplace=True)
			#insert missing dates
			numdays = 30
			base = datetime.datetime.today().date()
			date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
			dates = pd.DataFrame(date_list)
			dates.columns = ['date']
			#merge the complete dates with the dateframe
			df = pd.merge(dates,df, on=['date'], how='left')
			#order by dates
			df = df.sort_values('date',ascending=True)
			#make dates json serializable
			df['date'] = df.date.apply(json_serial)
			#get the difference instead of cumalation
			df[['Unique Views', 'Views', 'Messages', 'Orders']] = df[['Unique Views', 'Views', 'Messages', 'Orders']].diff()
			#fill all the NAs
			df[['Unique Views', 'Views', 'Messages', 'Orders']] = df[['Unique Views', 'Views', 'Messages', 'Orders']].fillna(value=0)


			#for bar chart
			#selecting the required columns
			dfb = df[['date','Views','Messages','Orders']]
			#adding the header to a list format
			dfbcolumn = [dfb.columns.values.tolist()]
			#adding the values to a list format
			dfb = dfb.values.tolist()
			#adding both together
			dfb = dfbcolumn + dfb

			#for line chart
			#selecting the required columns
			dfl = df[['date','Unique Views','Views']]
			#adding the header to a list format
			dflcolumn = [dfl.columns.values.tolist()]
			#adding the values to a list format
			dfl = dfl.values.tolist()
			#adding both together
			dfl = dflcolumn + dfl

			#for pie chart
			#selecting the required columns
			dfp = df[['Views','Messages','Orders']]
			dfpcolumn = [dfp.columns.values.tolist()]
			dfp = dfp.sum(axis=0)
			#think about how to do the minus the orders from messages and messages from views
			dfp = pd.DataFrame(dfp)
			# dfp.rename(columns={0:'count'}, inplace=True)
			dfp.reset_index(inplace=True)
			dfp.rename(columns={'index':'type', 0:'count'}, inplace=True)
			dfp = [dfp.columns.tolist()] + dfp.values.tolist()

		except:
			unotexist = "User data does not exist yet"


		context = {}

		try:
			context["unotexist"] = unotexist
		except:
			context["datab"] = json.dumps(dfb)
			context["datal"] = json.dumps(dfl)
			context["datap"] = json.dumps(dfp)

		try:
			context["dnotexist"] = dnotexist
		except:
			context["dataw"] = json.dumps(swdf)


		return render(request, template, context)




#This shit is still work in progress
class StudentChart(FormView):
	form_class = OrderChartForm
	template_name = 'scharts.html'


	# def get(self, request):
	# 	template = 'tcharts.html'
	# 	df = Order.objects.filter()

	# 	context = {
	# 		# 'datab': json.dumps(dfb),
	# 		# 'datal': json.dumps(dfl),
	# 		# 'datap': json.dumps(dfp)
	# 	}
	# 	return render(request, template, context)


	def get_context_data(self, **kwargs):
		context = super(StudentChart, self).get_context_data(**kwargs)

		enddate = datetime.datetime.now()
		tdelta = datetime.timedelta(days=5)
		startdate = enddate - tdelta
		startdate = startdate.date()
		
		qs = Order.objects.filter().distinct()

		subject_1 = self.request.GET.get("subject_1")
		subject_2 = self.request.GET.get("subject_2")
		subject_3 = self.request.GET.get("subject_3")
		level_type = self.request.GET.get("level")
		educational_level = self.request.GET.getlist("educational_level")
		expertise_type = self.request.GET.getlist("expertise_type")
		minimum_years = self.request.GET.get("minimum_years")
		group_tuition = self.request.GET.get("group_tuition")

		if subject_1:
			subject = subject_1
		elif subject_2:
			subject = subject_2
		else:
			subject = subject_3

		try:
			if subject and level_type:
				qs = qs.filter(
					Q(subject=subject, level=level_type)
				).distinct()
			# if educational_level:
			# 	qs = qs.filter(educational_level__in=educational_level)
			# if expertise_type:
			# 	qs = qs.filter(expertise_type__in=expertise_type)
			# if minimum_years and not minimum_years == '0':
			# 	qs = qs.filter(years_of_experience__gte=minimum_years)
			if group_tuition:
				qs = qs.filter(group_tuition=True)

			qs = qs.distinct()

			qs = qs.filter(date__range=[startdate, enddate], teacherorder=True, studentorder=True)



		except:
			pass


		return context


	def get_initial(self):
		if not self.request.GET.get('submit'):
			return self.initial.clear()
		else:
			self.initial.clear()
			for key in self.request.GET:
				try:
					if key == "submit":
						pass
					else:
						self.initial[key] = self.request.GET[key]
				except KeyError:
					pass
			return self.initial.copy()




