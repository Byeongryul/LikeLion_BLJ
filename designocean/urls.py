from django.contrib import admin
from django.urls import path, include
import DOservice.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',DOservice.views.home, name='home'),
    path('login/',DOservice.views.login, name='login'),
    path('mypage/',DOservice.views.mypage, name='mypage'),
    path('accounts/', include('allauth.urls')), 
    path('detail/',DOservice.views.detail, name = 'detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
