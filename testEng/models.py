from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User

# Create your models here.
class testQuestion(models.Model):
    question = models.CharField(max_length=1000)
    multichoice = models.BooleanField()

    def __str__(self):
        return self.question

class optionAnswer(models.Model):
    id_question = models.ForeignKey(testQuestion, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    isCorrect = models.BooleanField()

    def __str__(self):
        return self.content

class category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class quest_cate(models.Model):
    id_question = models.ForeignKey(testQuestion, on_delete=models.CASCADE)
    id_category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_question.question + ' - ' + self.id_category.name

class user(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class topic(models.Model):
    name = models.CharField(max_length=1000)
    content = models.TextField(max_length=10000)
    user = models.ForeignKey(User, default=1)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('testEng:topic')

class comment(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    content = models.CharField(max_length = 1000)

    def __str__(self):
        return self.content


class word(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length = 1000)
    meaning = models.CharField(max_length = 1000)
    pronunc = models.CharField(max_length = 1000)
    image = models.FileField()
    audio = models.FileField(default='')
    type = models.CharField(max_length = 1000)
    tolearn = models.BooleanField(default=False)
    # id_user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('testEng:dictionary')

class word_cate(models.Model):
    id_word = models.ForeignKey(word, on_delete=models.CASCADE, default=1)
    id_category= models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_word.name + ' - ' + self.id_category.name
