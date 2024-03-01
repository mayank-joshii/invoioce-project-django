from django.test import TestCase

# Create your tests here.
# tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice1 = Invoice.objects.create(date='2024-02-21', customer_name='Customer 1')
        self.invoice2 = Invoice.objects.create(date='2024-02-22', customer_name='Customer 2')

    def test_list_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_invoice(self):
        response = self.client.get(f'/invoices/{self.invoice1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Customer 1')

    # Add more test cases as needed

class InvoiceDetailViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date='2024-02-21', customer_name='Customer')
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Item 1', quantity=2, unit_price=10, price=20)

    def test_list_invoice_details(self):
        response = self.client.get(f'/invoice-details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_invoice_detail(self):
        response = self.client.get(f'/invoice-details/{self.invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Item 1')

    # Add more test cases as needed
