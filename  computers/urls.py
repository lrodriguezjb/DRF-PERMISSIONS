from computers.views import ComputersList, ComputersDetail
from django.urls import path


urlpatterns=[
    path('', ComputersList.as_view(), name='post_list'),
    path('<int:pk>/', ComputersDetail.as_view(), name='post_detail')
]