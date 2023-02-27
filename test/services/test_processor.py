import unittest
from unittest.mock import Mock, sentinel

from src.drivers.driver import Driver
from src.parsers.parser import Parser
from src.services.processor import Processor


class ProcessorTestCase(unittest.TestCase):

    def test_process(self) -> None:
        # Given
        # Mock Driver
        mock_driver = Mock(Driver)
        mock_driver.__enter__ = Mock(return_value=mock_driver)
        mock_driver.__exit__ = Mock(return_value=None)

        # Mock Parser
        mock_parser = Mock(Parser)
        mock_parser.receive_message.return_value = sentinel.some_object
        mock_parser.parse.return_value = None

        # When
        # Launch test
        Processor(mock_driver, mock_parser).run()

        # Then
        # Assertions
        mock_driver.__enter__.assert_called_once()
        mock_parser.receive_message.assert_called_once()
        mock_parser.parse.assert_called_once_with(sentinel.some_object)
        mock_driver.__exit__.assert_called_once()
