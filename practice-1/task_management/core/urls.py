from rest_framework.routers import DefaultRouter 

from .views import UserViewSet, ProjectViewSet, CategoryViewSet, PriorityViewSet, TaskViewSet 

 

router = DefaultRouter() 
router.register('users', UserViewSet) 
router.register('projects', ProjectViewSet) 
router.register('categories', CategoryViewSet) 
router.register('priorities', PriorityViewSet) 
router.register('tasks', TaskViewSet) 

urlpatterns = router.urls 