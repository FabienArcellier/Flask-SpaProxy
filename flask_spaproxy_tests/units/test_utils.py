import unittest

from flask_spaproxy.utils import is_url_for_file


class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_url_for_file_should_return_false_when_there_is_no_extension(self):
        # Assign
        url = "http://localhost:4000/path1/subpath"

        # Acts
        result = is_url_for_file(url)

        # Assert
        self.assertFalse(result)

    def test_is_url_for_file_should_return_true_when_there_is_an_extension(self):
        # Assign
        url = "http://localhost:4000/js/main.js"

        # Acts
        result = is_url_for_file(url)

        # Assert
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
