from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('api/chart/data/', views.BarChart.as_view(), name='api-chart-data'),

    path('irvine/', views.irvine, name='irvine'),
    path('sc/', views.santa_cruz, name='sc'),
    path('riverside/', views.riverside, name='riverside'),
    path('college/<int:pk>/', views.view_college, name='view-college'),
]
