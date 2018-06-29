from . import views
from django.urls import path


app_name = 'testapp'

urlpatterns = [

    path('',views.company,name='company_html'),
    path('create/',views.Createcompany,name='addcompany_html'),
    # path('edit/<pk>',views.LeadEdit.as_view(),name='LeadEdit'),
    # path('delete/<pk>',views.LeadDelete.as_view(),name='LeadDelete'),
    path('delete/<int:id>/', views.deleteview, name='delete1'),
    path('update/<int:id>/',views.Updatecompany,name='update'),


]