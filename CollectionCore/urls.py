from django.contrib import admin
from django.urls import path, re_path
from CollectionApp.views import DeleteCollection, EditCollection, InsertCollection, ReturnCollections
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Collection Project",
        default_version="v1",
        description="An simple collection project where you can Insert, Retrive, Delete and Update data."
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('return/', ReturnCollections.as_view()),
    path('update/', EditCollection.as_view()),
    path('delete/', DeleteCollection.as_view()),
    path('insert/', InsertCollection.as_view()),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
