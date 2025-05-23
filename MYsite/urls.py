
from django.contrib import admin
from django.urls import path , include
from website.views import *
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.urls import re_path
from django.conf import settings
from django.views.generic.base import TemplateView

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap , 
}
urlpatterns = [
    path('admin', admin.site.urls),
    path('', include("website.urls")),
    path('blog/', include("blog.urls")),
    path("accounts/",include("accounts.urls")),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    path("robots.txt" , include("robots.urls")),
    path("summernote/" , include("django_summernote.urls")),
    path("captcha" , include("captcha.urls")),

    ]
if settings.MAINTENANCE_MODE:
   urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='503.html'), name='maintenance'))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)