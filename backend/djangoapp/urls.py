from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, train_route, predict_route

urlpatterns = [
    path('', home, name='home'),
    path('train/', train_route, name='train_route'),
    path('predict/', predict_route, name='predict_route'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)