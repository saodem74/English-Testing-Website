from django.contrib import admin
from .models import quest_cate, category, optionAnswer, topic, word, user, testQuestion, comment, word_cate

# Register your models here.
admin.site.register(testQuestion)
admin.site.register(user)
admin.site.register(word)
admin.site.register(topic)
admin.site.register(optionAnswer)
admin.site.register(category)
admin.site.register(quest_cate)
admin.site.register(comment)
admin.site.register(word_cate)