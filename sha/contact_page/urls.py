from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('kurikindi-kawsay', views.kkc, name='kkc'),
    path('ceremonias', views.ceremonies, name='ceremonies'),
    path('training', views.training, name='training'),
    path('contacto', views.contact, name='contact'),
    path('proyecto', views.project, name='project'),
    path('thanks', views.thanks, name='thanks'),
    path('', views.twots, name='twots'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
