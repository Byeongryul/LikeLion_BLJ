from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LogoutView
from Designfeed.views import DesignfeedListView, DesignfeedDetailView, DesignfeedUpdateView, detail

from user.views import UserRegistrationView, UserLoginView, UserVerificationView, ResendVerifyEmailView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('feed/',DesignfeedListView.as_view(), name = 'home'),
    path('feed/<feed_id>',DesignfeedDetailView.as_view(),name='detail'),
    path('feed/create/',DesignfeedUpdateView.as_view()),
    path('feed/<feed_id>/update/', DesignfeedUpdateView.as_view()),

    path('user/create/', UserRegistrationView.as_view(template_name='user/user_model.html')),
    path('user/login/', UserLoginView.as_view()),
    path('user/<pk>/verify/<token>',UserVerificationView.as_view()),
    path('user/resend_verify_email/',ResendVerifyEmailView.as_view()),
    path('user/logout/',LogoutView.as_view()),

    path('accounts/',include('allauth.urls')),
    path('detail/',detail,name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
