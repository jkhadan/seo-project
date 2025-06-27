import unittest
import sys
from unittest.mock import patch, MagicMock
from main import get_stock_data, print_stock_data, save_and_print_data_to_db


class TestMain(unittest.TestCase):
    
    def test_get_api_key(self):
        original_argv = sys.argv
        sys.argv = ['main.py', 'test_api_key']
        
        from main import get_api_key
        result = get_api_key()
        self.assertEqual(result, 'test_api_key')
        
        sys.argv = original_argv

    def test_get_stock_data(self):
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'data': [{'date': '2024-01-15', 'close': 185.5}]}
            mock_get.return_value = mock_response
            
            result = get_stock_data('AAPL', 'test_key')
            self.assertEqual(result, [{'date': '2024-01-15', 'close': 185.5}])

    def test_print_stock_data(self):
        with patch('builtins.print') as mock_print:
            data = [{'date': '2024-01-15', 'close': 185.5}]
            print_stock_data(data)
            mock_print.assert_called()

    def test_save_and_print_data_to_db(self):
        with patch('pandas.DataFrame') as mock_df, \
             patch('sqlalchemy.create_engine') as mock_engine, \
             patch('builtins.print') as mock_print:
            
            mock_dataframe = MagicMock()
            mock_df.return_value = mock_dataframe
            
            mock_connection = MagicMock()
            mock_engine.return_value.connect.return_value.__enter__.return_value = mock_connection
            mock_connection.execute.return_value.fetchall.return_value = []
            
            data = [{'date': '2024-01-15', 'close': 185.5}]
            save_and_print_data_to_db(data)
            
            mock_dataframe.to_sql.assert_called_once()


if __name__ == '__main__':
    unittest.main()