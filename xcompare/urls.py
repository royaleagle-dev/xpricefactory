from django.urls import path
from . import views

app_name="xcompare"

urlpatterns=[
    path('', views.IndexView.as_view(), name="index"),
    path('history/', views.HistoryView.as_view(), name="history"),
    path('scrape/', views.ScrapeView.as_view(), name="scrape"),
]