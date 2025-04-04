from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from account import views



urlpatterns = [
    path("", views.home_view, name="home-view"),
    path("register-user/", views.register_user, name="register-user"),
    path("delete-user/<int:user_id>", views.delete_user, name="delete-user"),
    path("display-user/<int:user_id>", views.display_user, name="display-user"),
    path("edit-user/<int:user_id>", views.edit_user, name="edit-user"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
