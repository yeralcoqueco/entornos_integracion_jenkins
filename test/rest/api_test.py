import http.client
import os
import unittest
from unittest.mock import patch
from urllib.request import urlopen
import urllib.error


import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 3  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    @patch('app.util.convert_to_number', side_effect=ZeroDivisionError)
    def test_api_divide_by_zero(self, _convert_to_number):
        url = f"{BASE_URL}/calc/divide/1/0"
        with self.assertRaises(urllib.error.HTTPError) as context:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "Expected a 400 Bad Request response")


    def test_api_mutiply(self):
        url = f"{BASE_URL}/calc/mutiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    @patch('app.util.convert_to_number', side_effect=TypeError)
    def test_api_square_root_less_than_zero(self, _convert_to_number):
        url = f"{BASE_URL}/calc/square_root/-4"
        with self.assertRaises(urllib.error.HTTPError) as context:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "Expected a 400 Bad Request response")
        
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    @patch('app.util.convert_to_number', side_effect=TypeError)
    def test_api_log10_less_than_zero(self, _convert_to_number):
        url = f"{BASE_URL}/calc/log10/-1"
        with self.assertRaises(urllib.error.HTTPError) as context:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "Expected a 400 Bad Request response")
