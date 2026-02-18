from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('report',views.report_maker,name="report"),
    path('about',views.about_page,name = "about"),
    path('report_gen',views.report_genr,name ="report_gen"),
    path('regestration/',views.regestration,name ="regestration"),
    path('login/',views.login_page,name ="login"),
    path('logout/',views.logout_page,name = "logout"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




















