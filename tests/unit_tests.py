import unittest
import os
import main

from unittest.mock import patch, MagicMock
from requests.exceptions import RequestException
from utils.util import ensure_www

class TestWebFetcher(unittest.TestCase):

    def setUp(self):
        self.test_url = 'https://example.com'
        self.test_html_content = '<html><body><a href="https://link.com"></a><img src="image.jpg"/></body></html>'
        self.test_dir = 'example.com'

    @patch('main.requests.get')
    def test_save_website_content(self, mock_get):
        """Test saving website content without metadata and mirror flags."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = self.test_html_content
        mock_get.return_value = mock_response

        main.fetch_website(self.test_url, None, None)

        # Check if the file is created
        self.assertTrue(os.path.exists('example.com.html'))

        # Check file content to ensure correct content was saved
        with open('example.com.html', 'r') as f:
            saved_content = f.read()
            self.assertIn('<html><body>', saved_content)

    @patch('main.requests.get')
    def test_metadata_flag(self, mock_get):
        """Test fetching website content with metadata flag enabled."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = self.test_html_content
        mock_get.return_value = mock_response

        with patch('builtins.print') as mocked_print:
            main.fetch_website(self.test_url, fetch_metadata=True)

            mocked_print.assert_any_call(f"Metadata for {self.test_url}:")
            mocked_print.assert_any_call("-> Number of links: 1")
            mocked_print.assert_any_call("-> Number of images: 1")

    @patch('main.requests.get')
    @patch('utils.util.save_webpage')
    def test_mirror_flag(self, mock_save_webpage, mock_get):
        """Test mirroring the website with mirror flag enabled."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = self.test_html_content
        mock_get.return_value = mock_response

        mock_save_webpage.return_value = None

        main.fetch_website(self.test_url, None, True)

        self.assertTrue(os.path.exists(self.test_dir))

        # Verify that save_webpage was called with the correct arguments
        mock_save_webpage.assert_called_with(ensure_www(self.test_url), project_folder=os.path.join('/usr/src/app/', self.test_dir), bypass_robots=True)

    @patch('main.requests.get')
    def test_fetch_website_failure(self, mock_get):
        """Test handling failure when fetching website content."""
        mock_get.side_effect = RequestException("Connection error")

        with patch('builtins.print') as mocked_print:
            main.fetch_website(self.test_url, None, None)
            mocked_print.assert_any_call(f"Error fetching {self.test_url}: Connection error")

    # Clean up files after test run
    def tearDown(self):
        if os.path.exists('example.com.html'):
            os.remove('example.com.html')
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)


if __name__ == '__main__':
    unittest.main()
