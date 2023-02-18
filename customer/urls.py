from django.urls import path
from customer import views

urlpatterns = [
    path("register/",views.SignUpForm.as_view(),name="signup"),
    path("",views.SignView.as_view(),name="login"),
    path("home",views.IndexView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("product/<int:id>/carts/add",views.AddToCart.as_view(),name="cart-add"),
    path("customer/carts/all",views.CartListView.as_view(),name="cart-list"),
    path("cart/<int:id>/change",views.CartRemoveView.as_view(),name="cart-change"),
    path("orders/add/<int:id>",views.MakeOrderView.as_view(),name="created-order"),
    path("orders/all",views.MyOrderView.as_view(),name="my-order"),
    path("orders/<int:id>/change",views.OrderCancelView.as_view(),name="order-cancel"),
    path("offers/all",views.DiscountProductsView.as_view(),name="offer-list"),
    path("review/<int:id>/add",views.ReviewCreate.as_view(),name="review-add"),
    path("logout",views.signout_view,name="signout")
        
    
]
