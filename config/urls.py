
from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse

# family = ["papa ", "maman ", "enfants "]

# def test_view(request):
#     test = {
#         "papa1": "Mpoyi"
#     }
#     return HttpResponse(family)




urlpatterns = [
    # path('test/', test_view),
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
