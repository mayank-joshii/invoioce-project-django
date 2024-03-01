from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from home.views import InvoiceViewSet
from home.views import InvoiceDetailViewSet

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename = "invoices")
router.register(r'invoicedetail', InvoiceDetailViewSet, basename = "invoicedetail")

urlpatterns = [
    path('', include(router.urls)),
]