
from django.contrib import admin
from django.urls import path, include


from rest_framework.routers import DefaultRouter
from myapp.views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
