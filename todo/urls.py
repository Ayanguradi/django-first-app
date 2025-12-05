from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add-task/',views.add_task,name='add-task'),
]