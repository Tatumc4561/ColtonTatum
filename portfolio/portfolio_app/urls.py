from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("section_two/", views.section_two, name="two"),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
