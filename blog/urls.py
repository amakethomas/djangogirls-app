from.import views
from django.urls import path




urlpatterns = [
  path('blog/', views.post_list, name='post_list')
]