from django.contrib import admin
from django.urls import path, include
from rest_api import views
from rest_framework.routers import DefaultRouter
from rest_api.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

# Simple ViewSet
# router.register("std_api", views.Std_viewset, basename='student')

# Model ViewSet
router.register("std_api", views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/', views.ExampleView.as_view()),
    path('admin/', admin.site.urls),
    path('stdinfo/<int:pk>/', views.student_detail),
    path('stdinfo/', views.student_list),
    path('createStudent/', views.createStudent),
    path('deleteStudent/', views.deleteStudent),
    path('StudentApi/', views.StudentApi.as_view()),
    path('class_Api', views.class_Api.as_view()),
    path('class_Api/<int:pk>/', views.class_Api.as_view()),
    path('StdView', views.StdView.as_view()),
    path('StdCreate', views.StdCreate.as_view()),
    path('concrete_Api', views.concrete_Api.as_view()),
    path('concrete_Apis/<int:pk>/', views.concrete_Apis.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('jwt-gettoken/', TokenObtainPairView.as_view(), name='jwt-token'),
    path('jwt-refreshtoken/', TokenRefreshView.as_view(), name='jwt-refreshtoken'),
    path('jwt-verifytoken/', TokenVerifyView.as_view(), name='verify_token'),


]
