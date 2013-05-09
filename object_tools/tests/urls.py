try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import object_tools
object_tools.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^object-tools/', include(object_tools.tools.urls)),
)
