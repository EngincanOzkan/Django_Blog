from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import post
from .forms import postForm, commentForm
from django.contrib import messages
from django.utils.text import slugify
# Create your views here.^

def  post_index(request):
    posts = post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request,slug):
    selectedpost = get_object_or_404(post, slug=slug)

    form = commentForm(request.POST or None)

    if form.is_valid():
        donecomment = form.save(commit=False)
        donecomment.post = selectedpost
        donecomment.save();
        return HttpResponseRedirect(selectedpost.get_absolute_url())

    context = {
       'post': selectedpost,
       'form': form,
    }
    return render(request, 'post/detail.html', context)

def post_create(request):

    if not request.user.is_authenticated:
        return Http404()

    form = postForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        donepost = form.save(commit=False)
        donepost.user = request.user
        donepost.save();
        messages.success(request, 'Başarılı bir şekilde oluşturuldu.')
        return HttpResponseRedirect(donepost.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)



def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    selectedpost = get_object_or_404(post, slug=slug)
    form = postForm(request.POST or None, request.FILES or None, instance=selectedpost)
    if form.is_valid():
        donepost = form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi.')
        return HttpResponseRedirect(donepost.get_absolute_url())
    context = {
         'form': form,
    }

    return render(request, 'post/form.html', context)

def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    selectedpost = get_object_or_404(post, slug=slug)
    selectedpost.delete()
    return redirect('post:index')