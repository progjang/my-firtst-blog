from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^$', lambda request: redirect('blog:post_list')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]
