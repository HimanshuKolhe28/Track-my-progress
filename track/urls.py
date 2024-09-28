
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from track.views import ProfileViewSet,SprintsViewSet,TaskStatusViewSet,TaskViewSet


router = routers.DefaultRouter()

router.register('profile', ProfileViewSet)
router.register('Sprints',SprintsViewSet)
router.register('TaskStatus',TaskStatusViewSet)
router.register('taskView',TaskViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
]+router.urls