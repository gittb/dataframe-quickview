import unittest
import pandas as pd
from flask_testing import TestCase
from dataframe_quickview import app, quickview

class TestQuickView(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 4, 6, 8, 10],
            'C': [3, 6, 9, 12, 15]
        })

        app.config['df'] = self.df

    def test_dataframe_display(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<th>A</th>', response.data)
        self.assertIn(b'<td>1</td>', response.data)
        self.assertIn(b'<td>10</td>', response.data)

    def test_histogram_data(self):
        response = self.client.post('/histogram', data={'column': 'A'})
        self.assertEqual(response.status_code, 200)
        histogram_data = {int(k): v for k, v in response.json.items()}
        self.assertEqual(histogram_data, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1})


if __name__ == '__main__':
    unittest.main()
