
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 6
    context_object_name = "post_list"

    def get_queryset(self, **kwargs):
        return Post.objects.filter(presentar=True).order_by("-publicado")



class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

    
def mostrar_sobre_nosotros(request):
      return render(request, "sobrenosotros.html")  


class agregarPost(CreateView):
    model = Post
    fields = [
        "titulo",
        "slug",
        "cuerpo",
        "presentar",
        "autor"
    ]
    template_name = 'agregarpost.html'
    success_url = "/"
    
    def agregarPost(request):
      return render(request, "agregarpost.html") 
  

class DeletePost (DeleteView):
 model = Post
 template_name = "borrarpost.html"
 success_url ="/"
