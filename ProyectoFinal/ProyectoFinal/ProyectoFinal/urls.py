"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
import blog.views as views
from django.urls import  re_path as url
from django.conf.urls.static import static
from django.conf import settings
from blog.views import DeletePost


urlpatterns = [


    url(r'^admin/', admin.site.urls),
    url(r'^$', views.PostList.as_view(), name='home'),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post'),
    url(r"sobrenosotros.html/", views.mostrar_sobre_nosotros),
    url(r"agregarpost.html/", views.agregarPost.as_view(), name= 'agregarpost'),
    url(r"^borrarpost.html/", DeletePost.as_view(), name="delete_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)