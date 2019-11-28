from django.conf.urls import url
from toys import views

# The urlpatterns list makes it possible to route URLs to views. The code
# calls the django.conf.urls.url function with the regular expression that has to
# be matched and the view function defined in the views module as arguments
# to create a RegexURLPattern instance for each entry in the urlpatterns list
urlpatterns = [
    url(r'^toys/$', views.toy_list),
    url(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail)
]
