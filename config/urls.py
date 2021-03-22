from django.conf                import settings
from django.conf.urls.static  import static
from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse




urlpatterns = [
    # path('test/', test_view),
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:

    #import debug_toolbar

    urlpatterns = [

        
        #path('__debug__/',   include(debug_toolbar.urls)),

    ] + urlpatterns

    urlpatterns = urlpatterns + static(
                            settings.STATIC_URL, document_root=settings.STATIC_ROOT
                        )
    urlpatterns = urlpatterns + static(
                            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
                        )





# family = ["papa ", "maman ", "enfants "]

# def test_view(request):
#     test = {
#         "papa1": "Mpoyi"
#     }
#     return HttpResponse(family)

