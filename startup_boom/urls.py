
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django_email_verification import urls as mail_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
   
    path('mails/', include(mail_urls)),

    ##forgot password build 
    # 1. submit email form --> PasswordResetView.as_view()
    # 2. email sent success message --> PasswordResetDoneView.as_view()
    # 3. link to password reset form --> PasswordResetConfirmView.as_view()
    # 4. password successfully changed --> PasswordResetCompleteView.as_view()

    path('reset_password/', 
     auth_views.PasswordResetView.as_view(template_name = "accounts/resetPassword.html"), 
     name='reset_password'),

    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name = "accounts/resetDone.html"),
     name='password_reset_done'),

    path('reset/<slug:uidb64>/<slug:token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/resetConfirm.html"), 
     name='password_reset_confirm'),
    
    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/resetComplete.html"),
     name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
