import profile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Pic
from .forms import PicForm, ReviewForm


# Create your views here. 
def pic(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    pics = Pic.objects.filter(title__icontains=search_query)
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(pics, results)
 
    try:
        pics= paginator.page(page)
    except PageNotAnInteger:
        page=1
        pics = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        pics = paginator.page(page)
    
    context = {'pic': pics, 'paginator':paginator}
    return render(request, 'pic/pics.html', context)

def picture(request, pk):
    pictureObj = Pic.objects.get(id=pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.picture = pictureObj
        review.owner = request.user.profile 
        review.save()
        pictureObj.getVoteCount
        messages.success(request, 'Successfully voted')
        return redirect('picture', pk=pictureObj.id)

    return render(request, 'pic/picture.html', {'picture':pictureObj, 'form':form}) 

@login_required(login_url="login")
def createPicture(request):
    profile = request.user.profile
    form = PicForm()

    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.owner = profile
            picture.save()
            return redirect('pic')
    context = {'form':form}
    return render(request, 'pic/picture_form.html', context)

@login_required(login_url="login")
def updatePicture(request, pk):
    profile = request.user.profile 
    picture = profile.pic_set.get(id=pk)
    form = PicForm(instance=picture)

    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES , instance=picture)
        if form.is_valid():
            form.save()
            return redirect('pic')
    context = {'form':form}
    return render(request, 'pic/picture_form.html', context)

@login_required(login_url="login")
def deletePicture(request, pk):
    profile = request.user.profile 
    picture = profile.pic_set.get(id=pk)
    if request.method == 'POST':
        picture.delete()
        return redirect('pic')
    context = {'object':picture}
    return render(request, 'pic/delete_template.html', context)