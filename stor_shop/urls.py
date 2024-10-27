from django.urls import path
from .views import TaskViewSet
from django.urls import path, include


urlpatterns = [
    path('', TaskViewSet.as_view({'get':'list', 'post': 'create'}),
         name='task_list'),
    path('accounts/', include('allauth.urls')),
    path('<int:pk>/',TaskViewSet.as_view({'get':'retrieve',
                                          'put': 'update',
                                          'delete':'destroy'}),name='tsk_detail' )


]