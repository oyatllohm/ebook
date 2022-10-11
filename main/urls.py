from django.urls import path
from .views import CategoryApiView , BookApiView ,Get_student,Downland_ApiView

categorys_view = CategoryApiView.as_view({"get":"list"})
categoris_id_view = CategoryApiView.as_view({"get":"retrive"})
app_name =  'main'
urlpatterns = [
    path('get_student',Get_student.as_view(),name='get_student'),
    path('categories/<int:pk>',categoris_id_view, name="category_detail_view"),
    path('categories',categorys_view, name="categories"),
    path('book',BookApiView.as_view(),name='book'),
    path('downland/<int:pk>',Downland_ApiView.as_view(),name= 'downland'),
]