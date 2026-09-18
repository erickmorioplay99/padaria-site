from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pedidos.views import tela_selecao # <-- Isso traz a sua tela de seleção do totem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tela_selecao, name='tela_selecao'), # <-- CORRIGIDO: Isso diz ao Django para abrir seu totem na página inicial!
]

# Libera o acesso visual às fotos de queijos, massas, etc.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
