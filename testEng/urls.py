from django.conf.urls import url
from . import views

app_name = 'testEng'
urlpatterns = [
    # /testEng/
    url(r'^$', views.index, name = 'index'),

    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),

    url(r'^(?P<testQuestion_id>[0-9]+)/$', views.detail, name="detail"),

    url(r'^topic/$', views.gettopic, name = 'topic'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.detailtopic, name = 'detail-topic'),
    url(r'^topic/topicadd/$', views.TopicCreate.as_view(), name='topic-add'),
    url(r'^topic/createtopic/$', views.CreateTopicFormView.as_view(), name = 'createtopic'),
    url(r'^topic/(?P<pk>[0-9]+)/updatetopic/$', views.TopicUpdate.as_view(), name='topic-update'),
    url(r'^topic/(?P<pk>[0-9]+)/deletetopic/$', views.TopicDelete.as_view(), name='topic-delete'),

    url(r'^dictionary/$', views.dictionary, name = 'dictionary'),
    url(r'^dictionary/dictionaryTolearn/$', views.dictionaryTolearn, name = 'dictionaryTolearn'),
    url(r'^dictionary/wordadd/$', views.WordCreate.as_view(), name='word-add'),
    url(r'^dictionary/(?P<pk>[0-9]+)/updateword/$', views.WordUpdate.as_view(), name='word-update'),
    url(r'^dictionary/(?P<pk>[0-9]+)/deleteword/$', views.WordDelete.as_view(), name='word-delete'),
    url(r'^dictionary/createword/$', views.CreateWordFormView.as_view(), name = 'createword'),
    url(r'^dictionary/(?P<word_id>[0-9]+)/tolearn/$', views.tolearn, name='tolearn'),

    url(r'^testing/$', views.gettest, name = 'testing'),
    # url(r'^create_word/$', views.create_word, name='create_word'),
]
# <!--<form action="{% url '#' quest.id %}" method="post">-->