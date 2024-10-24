from django.test import TestCase
from django.urls import reverse
from .models import Orders
from .forms import OrderForm
class OrdersModelTests(TestCase):

    def test_orders_creation(self):
        order = Orders.objects.create(
            oid=1,
            fname='Uma Shankar',
            lname='Singh',
            price=235,
            mail='umash@gmail.com',
            addr='Sector 49'
        )
        self.assertEqual(order.fname, 'Uma Shankar')
        self.assertEqual(order.price, 141)

    def test_string_representation(self):
        order = Orders.objects.create(
            oid=2,
            fname='Uma Shankar',
            lname='Singh',
            price=49.99,
            mail='jane@example.com',
            addr='Sector 49'
        )
        self.assertEqual(str(order), 'Uma Shankar')

class OrdersViewsTests(TestCase):

    def setUp(self):

        self.order = Orders.objects.create(
            oid=1,
            fname='Abhishek',
            lname='Singh',
            price=99.99,
            mail='abhiakauma@gmail.com',
            addr='123 Main St'
        )

    def test_order_form_view_get(self):
        response = self.client.get(reverse('order_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/orders.html')
        self.assertIsInstance(response.context['form'], OrderForm)

    def test_show_view(self):
        response = self.client.get(reverse('show_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/show.html')
        self.assertContains(response, 'Abhishek')
    
    def test_update_view_get(self):
        response = self.client.get(reverse('update_url', args=[self.order.oid]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/orders.html')
        self.assertEqual(response.context['form'].instance, self.order)

    def test_update_view_post_valid(self):
        response = self.client.post(reverse('update_url', args=[self.order.oid]), {
            'oid': 1,
            'fname': 'Abhishek',
            'lname': 'Roy',
            'price': 89.99,
            'mail': 'aroy@example.com',
            'addr': 'Samstipur'
        })
        self.assertRedirects(response, reverse('show_url'))