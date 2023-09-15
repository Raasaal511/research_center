from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from .models import Test, Lab, Indicator


class TestAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        lab = Lab.objects.create(name='center lab',)
        self.test = Test.objects.create(started_at='2023-09-14T19:58:00Z',
                                        completed_at='2023-09-14T20:58:00Z',
                                        lab_id=lab.id)

    def test_get_result_test(self):
        url = reverse('result-test', kwargs={'test_id': self.test.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['id']), str(self.test.id))
        self.assertEqual(str(response.data['lab_id']), str(self.test.lab_id))
        self.assertEqual(len(response.data['results']), 0)


class LabAPITestCase(TestCase):
    def setUp(self):
        self.lab = Lab.objects.create(name='center lab')

    def test_get_lab_list(self):
        client = APIClient()
        response = client.get(reverse('labs-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_lab_detail(self):
        client = APIClient()
        response = client.get(reverse('labs-detail', kwargs={'pk': self.lab.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.lab.name)


class IndicatorAPITestCase(TestCase):
    def setUp(self):
        self.indicator = Indicator.objects.create(name="Indicator 1", description="Description")

    def test_get_indicator_list(self):
        client = APIClient()
        response = client.get(reverse('indicator-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_indicator_detail(self):
        client = APIClient()
        response = client.get(reverse('indicator-detail', kwargs={'pk': self.indicator.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.indicator.name)
