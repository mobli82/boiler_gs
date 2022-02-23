from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('post/', views.boiler_post_temp, name='statistics'),
    path('monitor/', views.bolier_monitor_view, name='monitor'),
    path('burn_settings/', views.burn_settings_view, name='burn-settings'),
]