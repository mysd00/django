from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

#After changing models, this create migrations:   python manage.py makemigrations polls
#And this one will apply the changes to database: python manage.py migrate polls
#This one is giving us information:               python manage.py sqlmigrate polls 0001
#This checks for problems:                        python manage.py check

class Question(models.Model):
    # Name of the question, first parameter is somehow a substitute for a documentation, second is obligatory
    question_text = models.CharField('question asked', max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #That tells Django each Choice is related to a single Question.
    choice_text = models.CharField('choice possible',max_length=20)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Q_number(models.Model):   #It's doing shit for now
    number = models.IntegerField(default=5)
    def __str__(self):
        return self.number






class Survey(models.Model):
	name = models.CharField(max_length=400)
	description = models.TextField()

	def __unicode__(self):
		return (self.name)

	def questions(self):
		if self.pk:
			return Question1.objects.filter(survey=self.pk)
		else:
			return None

class Category(models.Model):
	name = models.CharField(max_length=400)
	survey = models.ForeignKey(Survey)

	def __unicode__(self):
		return (self.name)

def validate_list(value):
	'''takes a text value and verifies that there is at least one comma '''
	values = value.split(',')
	if len(values) < 2:
		raise ValidationError("The selected field requires an associated list of choices. Choices must contain more than one item.")

class Question1(models.Model):
	TEXT = 'text'
	RADIO = 'radio'
	SELECT = 'select'
	SELECT_MULTIPLE = 'select-multiple'
	INTEGER = 'integer'

	QUESTION_TYPES = (
		(TEXT, 'text'),
		(RADIO, 'radio'),
		(SELECT, 'select'),
		(SELECT_MULTIPLE, 'Select Multiple'),
		(INTEGER, 'integer'),
	)

	text = models.TextField()
	required = models.BooleanField()
	category = models.ForeignKey(Category, blank=True, null=True,)
	survey = models.ForeignKey(Survey)
	question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
	# the choices field is only used if the question type
	choices = models.TextField(blank=True, null=True,
		help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

	def save(self, *args, **kwargs):
		if (self.question_type == Question1.RADIO or self.question_type == Question1.SELECT
			or self.question_type == Question1.SELECT_MULTIPLE):
			validate_list(self.choices)
		super(Question1, self).save(*args, **kwargs)

	def get_choices(self):
		''' parse the choices field and return a tuple formatted appropriately
		for the 'choices' argument of a form widget.'''
		choices = self.choices.split(',')
		choices_list = []
		for c in choices:
			c = c.strip()
			choices_list.append((c,c))
		choices_tuple = tuple(choices_list)
		return choices_tuple

	def __unicode__(self):
		return (self.text)

class Response(models.Model):
	# a response object is just a collection of questions and answers with a
	# unique interview uuid
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	survey = models.ForeignKey(Survey)
	interviewer = models.CharField('Name of Interviewer', max_length=400)
	interviewee = models.CharField('Name of Interviewee', max_length=400)
	conditions = models.TextField('Conditions during interview', blank=True, null=True)
	comments = models.TextField('Any additional Comments', blank=True, null=True)
	interview_uuid = models.CharField("Interview unique identifier", max_length=36)

	def __unicode__(self):
		return ("response %s" % self.interview_uuid)

class AnswerBase(models.Model):
	question = models.ForeignKey(Question)
	response = models.ForeignKey(Response)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

# these type-specific answer models use a text field to allow for flexible
# field sizes depending on the actual question this answer corresponds to. any
# "required" attribute will be enforced by the form.
class AnswerText(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerRadio(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerSelect(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerSelectMultiple(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerInteger(AnswerBase):
	body = models.IntegerField(blank=True, null=True)

