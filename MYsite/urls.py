
from django.contrib import admin
from django.urls import path , include
from website.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from MYsite.setting.dev import DEBUG
from MYsite.view import *

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap , 
}
if DEBUG == False:
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
else:
    urlpatterns = [
        path('admin', comingsoon),
        path('', comingsoon),
        path('blog/', comingsoon),
        path("accounts/",comingsoon),
        path("sitemap.xml",comingsoon),
        path("robots.txt" , comingsoon),
        path("summernote/" , comingsoon),
        path("captcha" , comingsoon),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)