from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home import views
from order import views as orderviews

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/', include('product.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('product/', include('product.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('user/', include('user.urls'), name='user'),
    path('order/', include('order.urls')),
    path('shopcart/', orderviews.shopcart, name='shopcart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)