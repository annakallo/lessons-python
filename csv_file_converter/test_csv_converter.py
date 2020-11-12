import unittest
from csv_file_converter import csv_converter


class TestImportCsv(unittest.TestCase):
    """
    Test how the csv is read and writen.
    """
    def test_import_csv_original_invoices(self):
        """
        Tests if the the function imports correctly the csv file and if the list created with the data is correct.
        """
        file_name = 'facturas-iva-desglosado.csv'
        result = csv_converter.import_csv_original_invoices(file_name)
        self.assertEqual(len(result[0]), 24)
        self.assertEqual(type(result[0]['cod_fact']), str)
        self.assertEqual(type(result[0]['base']), str)
        # for r in result:
        #     print(r)

    def test_export_to_csv_processed_invoices(self):
        """
        Tests how a new csv created with the data.
        """
        data_csv = [{
                'Nº Factura': 'one',
                'Fecha': 1,
                'Proveedor': 1,
                'CIF': 1,
                'Base Imponible': 1,
                'Cuota IVA': 1,
                '%IVA': 1,
                'Ret': 1,
                '% Ret': 1,
                'Rec eq': 1,
                '% Rec eq': 1,
                'Total': 1,
                'Tipo gasto': 1
            },
            {
                'Nº Factura': 'two',
                'Fecha': 2,
                'Proveedor': 2,
                'CIF': 2,
                'Base Imponible': 2,
                'Cuota IVA': 2,
                '%IVA': 2,
                'Ret': 2,
                '% Ret': 2,
                'Rec eq': 2,
                '% Rec eq': 2,
                'Total': 2,
                'Tipo gasto': 2
            }
        ]
        result = csv_converter.export_to_csv_processed_invoices('output.csv', data_csv)

    def test_convert_original_to_processed_data(self):
        """
        Checks how the data is converted.
        """
        file_name = 'facturas-iva-desglosado.csv'
        data = csv_converter.import_csv_original_invoices(file_name)
        result = csv_converter.convert_original_to_processed_data(data)
        self.assertEqual(len(result[0]), 13)
        self.assertEqual(type(result[0]['Nº Factura']), int)
        self.assertEqual(type(result[0]['Fecha']), str)
        self.assertEqual(type(result[0]['Proveedor']), str)
        for line in result:
            print(line)
        export_file_name = 'apple.csv'
        csv_converter.export_to_csv_processed_invoices(export_file_name, result)


