import unittest
from csv_file_converter import csv_converter_binance
from decimal import Decimal


class TestImportCsv(unittest.TestCase):
    """
    Test how the csv is read and writen.
    """
    def test_import_csv_source_data(self):
        """
        Tests if the the function imports correctly the csv file and if the list created with the data is correct.
        """
        file_name = 'binance-futures-trade-history.csv'
        result = csv_converter_binance.import_csv_source_data(file_name)
        self.assertEqual(len(result[0]), 4)
        self.assertEqual(type(result[0]['date']), str)
        self.assertEqual(type(result[0]['amount']), Decimal)
        # for r in result:
        #     print(r)

    def test_export_to_csv_target_data(self):
        """
        Tests how a new csv created with the data.
        """
        data_csv = [{
            'Tipo': 'one',
            'Compra': 1,
            'Cur. Compra': 1,
            'Venta': 1,
            'Cur. Venta': 1,
            'Comision': 1,
            'Cur. Comision': 1,
            'Exchange': 1,
            'Grupo': 1,
            'Comentario': 1,
            'Fecha': 1
            },
            {
            'Tipo': 'two',
            'Compra': 2,
            'Cur. Compra': 2,
            'Venta': 2,
            'Cur. Venta': 2,
            'Comision': 2,
            'Cur. Comision': 2,
            'Exchange': 2,
            'Grupo': 2,
            'Comentario': 2,
            'Fecha': 2
            }
        ]
        result = csv_converter_binance.export_to_csv_target_data('tryout_target.csv', data_csv)

    def test_convert_source_to_target_data(self):
        """
        Checks how the data is converted.
        """
        file_name = 'binance-futures-trade-history.csv'
        data = csv_converter_binance.import_csv_source_data(file_name)
        result = csv_converter_binance.convert_source_to_target_data(data)
        csv_converter_binance.export_to_csv_target_data('result.csv', result)
        self.assertEqual(len(result[0]), 11)
        self.assertEqual(type(result[0]['Tipo']), str)
        self.assertEqual(type(result[0]['Fecha']), str)
        # for line in result:
        #     print(line)


