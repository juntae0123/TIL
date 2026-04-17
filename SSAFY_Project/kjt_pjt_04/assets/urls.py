from django.urls import path

from . import views

app_name = "assets"

urlpatterns = [
    path("", views.asset_list, name="asset_list"),
    path("<str:asset_id>/", views.asset_detail, name="asset_detail"),
    path("<str:asset_id>/posts/create/", views.post_create, name="post_create"),
    path("<str:asset_id>/posts/<int:post_pk>/", views.post_detail, name="post_detail"),
    path("<str:asset_id>/posts/<int:post_pk>/update/", views.post_update, name="post_update"),
    path("<str:asset_id>/posts/<int:post_pk>/delete/", views.post_delete, name="post_delete"),
]