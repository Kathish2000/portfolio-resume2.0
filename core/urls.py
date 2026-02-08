from django.urls import path
from .views import HomeView, AboutView, ExperienceView, ProjectListView, ContactView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]
