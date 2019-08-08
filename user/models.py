from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email=None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin): #유저 모델 재정의
    email = models.EmailField(verbose_name=_('email address'), unique=True, blank=False)
    name = models.CharField(_('name'),max_length=30,blank=True)
    is_staff = models.BooleanField(
        _('staff_status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts. '
        )
    )
    date_joined = models.DateTimeField('가입일',default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'          #이메일을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name']        #필수 입력값

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = ('_users')
        swappable = 'AUTH_USER_MODEL'
    
    def email_user(self, subjects, message, from_email=None, **kwargs):      #이메일 발송 메서드
        send_mail(subject, message, from_emial, [self.email], **kwargs)