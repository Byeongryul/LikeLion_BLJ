from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from Designfeed.models import DesignFeed
from django.contrib import messages
from django.conf import settings
# Create your views here.

class DesignfeedListView(TemplateView):
    template_name = 'home.html'
    queryset = DesignFeed.objects.all()
    def get(self, request, *args, **kwargs):
        ctx = {
            'feeds' : self.queryset.order_by('-created_at')
        }
        return self.render_to_response(ctx)

class DesignfeedDetailView(TemplateView):
    template_name = 'detail.html'
    queryset = DesignFeed.objects.all()
    pk_url_kwargs = 'feed_id'
    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        feed = queryset.filter(pk=pk).first()     
        if not feed:
            raise Http404('invalid pk')
        return feed

    def get(self, request, *args, **kwargs):
        feed = self.get_object()

        if not feed:
            raise Http404('invalid feed_id')
        ctx = {
            'feed' : feed
        }
        return self.render_to_response(ctx)

class DesignfeedUpdateView(TemplateView):
    login_url = settings.LOGIN_URL
    template_name = 'upload.html'
    queryset = DesignFeed.objects.all()
    pk_url_kwargs = 'feed_id'
    success_message = '피드가 저장되었습니다.'
    
    def get_object(self, queryset = None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        feed = queryset.filter(pk=pk).first()

        if pk and not feed:
            raise Http404('invalid pk')
        return feed

    def get(self, request, *args, **kwargs):
        feed = self.get_object()
        ctx = {
            'feed' : feed    
        }
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        post_data = {key : request.POST.get(key) for key in ('title', ' discription', 'author')}
        for key in post_data:
            if not post_data[key]:
                messages.error(self.request, '{} 값이 존재하지 않습니다.'.format(key),extra_tags='danger')
        if len(messages.get_messages(request)) == 0:
            if action == 'create':
                feed = DesignFeed.objects.create(**post_data)
                messages.success(self.request, self.success_message)
            elif action == 'update':
                feed = self.get_object()
                for key, value in post_data.items():
                    setattr(feed, key, value)
                feed.save()
                messages.success(self.request, self.success_message)
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')
            
            return HttpResponseRedirect('/feed/')
        ctx = {
            'feed' : self.get_object() if action == 'update' else None
        }
        return self.render_to_response(ctx)


def detail(request):
    return render(request,'detail.html')