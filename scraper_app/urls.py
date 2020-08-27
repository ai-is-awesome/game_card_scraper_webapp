from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'), 
	path('scrape/', views.scrape, name = 'scrape_url'), 
	path('temp/', views.scraper2, name=  'temp'), 
	path('temp_detail', views.scraper2_detail, name = 'temp_detail')
]







