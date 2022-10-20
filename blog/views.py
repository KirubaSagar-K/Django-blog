from django.shortcuts import render
from .models import post
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


posts = [
    {
        'author' : 'Stephen Hawkings',
        'title' : 'Theory Of Everything',
        'content' : 'Origin Of Universe',
        'posted' : 'May 6, 2010'
    },
    {
        'author' : 'Yual Noah Harari',
        'title' : 'Sapiens',
        'content' : 'History of humankind',
        'posted' : 'August 20, 2020'
    }
]

def  home(request):
    context = {
        'posts' : post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class postlist(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-posted_at']
    paginate_by = 5

class postdetail(DetailView):
    model = post

class postcreate(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class postupdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class postdelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/blog'

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})