from django.urls import path
from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('products/',views.product_list,name='product_list'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path(
    'product/<slug:slug>/',
    views.product_detail,
    name='product_detail'
),
path(
    'category/<slug:slug>/',
    views.category_products,
    name='category_products'
),
path(
    "wishlist/toggle/",
    views.toggle_wishlist,
    name="toggle_wishlist"
),
path(
    "wishlist/",
    views.wishlist,
    name="wishlist"
),
path(
    "cart/add/",
    views.add_to_cart,
    name="add_to_cart",
),

]
