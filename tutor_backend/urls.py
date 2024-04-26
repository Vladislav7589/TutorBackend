"""
URL configuration for tutor_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from tutor_app import views
from django.urls import include, path

from tutor_app.views import SubjectViewSet

router = SimpleRouter()
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index")
    # Добавьте другие маршруты...
]
urlpatterns += router.urls
