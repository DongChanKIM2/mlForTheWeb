#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin
from books_recsys_app.api import UsersList
import books_recsys_app.views
import rest_framework_swagger
'''
#working on django 1.7
urlpatterns = patterns('',
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', 'books_recsys_app.views.home', name='home'),
    url(r'^auth/', 'books_recsys_app.views.auth', name='auth'),   
    url(r'^signout/','books_recsys_app.views.signout',name='signout'),
    url(r'^rate_movie/','books_recsys_app.views.rate_movie',name='rate_movie'),
    url(r'^movies-recs/','books_recsys_app.views.movies_recs',name='movies_recs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users-list/',UsersList.as_view(),name='users-list')
)
'''
urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', books_recsys_app.views.home, name='home'),
    url(r'^auth/', books_recsys_app.views.auth, name='auth'),   
    url(r'^signout/',books_recsys_app.views.signout,name='signout'),
    url(r'^rate_movie/',books_recsys_app.views.rate_movie,name='rate_movie'),
    url(r'^movies-recs/',books_recsys_app.views.movies_recs,name='movies_recs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users-list/',UsersList.as_view(),name='users-list')
]