"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include,re_path
from book  import views
print("in urls.py")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage,name="homepage"),
    path('show-all-books/', views.show_all_books,name="show_all_books"),
    path("edit/<int:id>/",views.edit_data,name="edit"),
    path("delete/<int:id>/",views.delete_data,name="delete"),
    path("delete_all/",views.delete_all,name="delete_all"),
    path("soft_delete/<int:id>",views.soft_delete,name="soft_delete"),
    path("show_soft_delete/>",views.show_soft_delete,name="show_soft_delete"),
    path("restore/<int:id>",views.restore,name="restore"),
    path("soft_delete_all/>",views.soft_delete_all,name="soft_delete_all"),
    path('__debug__/', include('debug_toolbar.urls')),
    path("form-home/",views.form_home,name="form_home"),
    path("post-list/",views.post_list,name="post_list"), ####paging
    

    ####Class Based 
    path("home-cbv/",views.Homepage.as_view(),name="homepage"),
    path('Temp-view/',views.Temp_view.as_view(),name="Temp_view"),
    path('emp-gencreate/',views.Employeecreate.as_view(),name="Employeecreate"),
    path('emp-retr/',views.EmployeeRetrieve.as_view(),name="EmployeeRetrieve"),
    path('emp-retr/<int:pk>/',views.EmployeeDetail.as_view(),name="EmployeeDetail"),
    path('emp-update/<int:pk>/',views.EmployeeUpdate.as_view(),name="EmployeeUpdate"),
    path('emp-delete/<int:pk>/',views.EmployeeDelete.as_view(),name="EmployeeDelete")
]


urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]
