from django.conf.urls import url

from hash_tags import views

urlpatterns =  [
    url(r'^', views.twitter_hashtags, name='hash_tags')
]