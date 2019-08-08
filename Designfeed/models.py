from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
def user_path(instance, filename): #파라미터 instance는 DesignFeed 모델을 의미 filename은 업로드 된 파일의 파일 이름

    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정

    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png

class DesignFeed(models.Model):
    title       = models.CharField('제목', max_length=126, null=False)
    #owner       = models.ForeignKey(settings.AUTH_USER_MODEL)    # 로그인 한 사용자, many to one relation
    image       = models.ImageField(upload_to = user_path)     # 어디로 업로드 할지 지정
    discription = models.TextField('내용', null=False)
    author      = models.CharField('작성자', max_length=16, null=False)
    created_at  = models.DateTimeField('작성일', default = timezone.now)

    created_at.editable = True                                     # created의 editable 속성에 True를 설정.

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)