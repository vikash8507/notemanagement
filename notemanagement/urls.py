from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from user.views import CustomLoginView

from user.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('user.urls')),
    path('notes/', include('note.urls')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
