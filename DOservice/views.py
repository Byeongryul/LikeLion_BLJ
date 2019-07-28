from django.shortcuts import render, get_object_or_404

from .models import DesignPiece
# Create your views here.
def home(request):
    pieces = DesignPiece.objects
    return render(request,'home.html',{'pieces':pieces})
def new(request):
    return render(request,'new.html')

def create(request):
    piece = DesignPiece()
    piece.title = request.GET['title']
    piece.description = request.GET['body']   
    piece.pub_data = timezone.datetime.now()
    piece.image = request.GET['image']
    piece.save()
    return redirect('/detail/' + str(piece.id))

def login(request):
    return render(request,'login.html')
    
def mypage(request):
    return render(request,'mypage.html')

def detail(request):
    return render(request, 'detail.html')