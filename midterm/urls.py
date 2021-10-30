from django.urls import path
from .import views

app_name = 'midterm'

## function-based view
### Generic view (class-based view)
urlpatterns=[
    # ex: /midterm/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /midterm/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /midterm/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /midterm/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]