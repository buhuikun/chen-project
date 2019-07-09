import xadmin
from .models import *
xadmin.site.register(Article)
xadmin.site.register(Ads)
xadmin.site.register(Tag)
xadmin.site.register(Category)
