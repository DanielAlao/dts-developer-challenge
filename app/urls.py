"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from webapp import views  # for dashboard
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from ms_identity_web.django.msal_views_and_urls import MsalViews

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('webapp.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('dashboard/', views.task_dashboard, name='task_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task_status,
         name='update_task_status'),
    path('delete/<int:task_id>/', views.delete_user_task, name='delete_user_task'),
    path('', views.index, name='index'),  # default page
    path('auth/401/', views.unauth_401, name='unauth_401'),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/',
         include(msal_urls)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
