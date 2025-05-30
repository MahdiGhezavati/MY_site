from django.contrib.sitemaps import Sitemap
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.poblished_date