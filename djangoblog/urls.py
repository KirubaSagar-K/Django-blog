from re import template
from django.contrib import admin
from django.urls import path, include
from users import views as user_view
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
     path('profile/', user_view.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
     path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/', include('blog.urls'))
] 

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

