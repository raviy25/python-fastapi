from unittest import TestCase
from services.scrape_service import WebScraper

from requests import Session
from requests.models import Response
from unittest.mock import patch, Mock

class ScrapeServiceTest(TestCase):

    @patch.object(Session, 'get')
    def test_service(self, mock_get):
        mock_response = Mock(spec=Response)
        mock_response.content = "<tr>Hello<tr>"
        mock_get.return_value = mock_response

        sut = WebScraper("http://test")
        result = sut.scrape()
        # Assert
        self.assertEqual(result.find("tr").get_text(), "Hello")
