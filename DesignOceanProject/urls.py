from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LogoutView
from Designfeed.views import DesignfeedListView, DesignfeedDetailView, DesignfeedUpdateView, detail

from user.views import UserRegistrationView, UserLoginView, UserVerificationView, ResendVerifyEmailView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('feed/',DesignfeedListView.as_view(), name = 'home'), #메인페이지
    path('feed/<feed_id>',DesignfeedDetailView.as_view(),name='detail'), #디테일 페이지
    path('feed/create/',DesignfeedUpdateView.as_view()), #업로드 페이지
    path('feed/<feed_id>/update/', DesignfeedUpdateView.as_view()), #업데이트 페이지

    path('user/create/', UserRegistrationView.as_view(template_name='user/user_model.html')), #유저 생성 페이지
    path('user/login/', UserLoginView.as_view()), #유저 로그인 페이지
    path('user/<pk>/verify/<token>',UserVerificationView.as_view()), #유저 토큰 발급 페이지
    path('user/resend_verify_email/',ResendVerifyEmailView.as_view()), #아무튼 이메일 관리 페이지
    path('user/logout/',LogoutView.as_view()), #로그아웃 페이지
 
    path('accounts/',include('allauth.urls')), #소셜 로그인 페이지
    path('detail/',detail,name='detail'), #디테일 페이지 확인 용 신경쓸 필요 없음
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
