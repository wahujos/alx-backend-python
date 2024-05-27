#!/usr/bin/env python3
"""
In this task you will write the first unit test for utils.access_nested_map.
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it is supposed to.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a,"), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """
        Implement TestAccessNestedMap.test_access_nested_map_exception.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), missing_key)


class TestGetJson(unittest.TestCase):
    """
    class and implement the TestGetJson.test_get_json
    method to test that utils.get_json returns the expected
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Use unittest.mock.patch to patch requests.get.
        Make sure it returns a Mock object with a json
        method that returns test_payload which you parametrize
        alongside the test_url that you will pass to get_json
        with the following inputs:
        """
        with patch('requests.get') as m_get:
            m_response = Mock()
            m_response.json.return_value = test_payload
            m_get.return_value = m_response
            result = get_json(test_url)
            m_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
