from django.urls import path
from .views import dispatch_report, login_view, logout_view, admin_dashboard, record_dispatch, store_manager_dashboard, update_product

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("store-manager-dashboard/", store_manager_dashboard, name="store_manager_dashboard"),
    path('update-product/<int:product_id>/', update_product, name='update_product'),
    path("record-dispatch/", record_dispatch, name="record_dispatch"),
    path("dispatch-report/", dispatch_report, name="dispatch_report"),
]

