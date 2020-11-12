import csv
import os
from decimal import Decimal
import sys


def import_csv_source_data(file_name):
    """
    Imports a csv file with the original entries and stores it in an array.
    Returns the array.
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + file_name) as file:
        reader = csv.DictReader(file, delimiter=',')
        csv_data = []
        for line in reader:
            csv_data.append(
                {
                    'date': line['Date(UTC)'],
                    'type': line['Type'],
                    'amount': Decimal(line['Amount']),
                    'asset': line['Asset']
                }
            )
    return csv_data


def export_to_csv_target_data(export_file_name, csv_data):
    """
    Export a csv file with the data extracted from the source data.
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + export_file_name, mode='w') as file:
        fieldnames = ['Tipo', 'Compra', 'Cur. Compra', 'Venta', 'Cur. Venta',
                      'Comision', 'Cur. Comision', 'Exchange', 'Grupo', 'Comentario', 'Fecha']
        writer = csv.DictWriter(file, lineterminator='\n', fieldnames=fieldnames)

        writer.writeheader()
        for line in csv_data:
            writer.writerow({
                'Tipo': line['Tipo'],
                'Compra': line['Compra'],
                'Cur. Compra': line['Cur. Compra'],
                'Venta': line['Venta'],
                'Cur. Venta': line['Cur. Venta'],
                'Comision': line['Comision'],
                'Cur. Comision': line['Cur. Comision'],
                'Exchange': line['Exchange'],
                'Grupo': line['Grupo'],
                'Comentario': line['Comentario'],
                'Fecha': line['Fecha']
            })


def convert_source_to_target_data(csv_source_data):
    """
    Converts the data from the original csv to what we want to export.
    """
    csv_data_processed = []
    for line in csv_source_data:
        # setting the type
        comentario = ''
        if line['type'] == 'TRANSFER':
            type_of_entry = 'Transfer'
        elif line['type'] == 'COMMISSION':
            type_of_entry = 'Other Fee'
            comentario = 'Commission'
        elif line['type'] == 'REALIZED_PNL' and line['amount'] > 0:
            type_of_entry = 'Derivatives / Futures Profit'
        elif line['type'] == 'REALIZED_PNL' and line['amount'] < 0:
            type_of_entry = 'Derivatives / Futures Loss'
        else:
            type_of_entry = 'Unknown type'
        # setting the compra venta based if the amount is positive or negative
        if line['amount'] >= 0:
            compra = line['amount']
            cur_compra = line['asset']
            venta = ''
            cur_venta = ''
        else:
            compra = ''
            cur_compra = ''
            venta = line['amount']
            cur_venta = line['asset']
        # filling up the new array
        csv_data_processed.append(
            {
                'Tipo': type_of_entry,
                'Compra': compra,
                'Cur. Compra': cur_compra,
                'Venta': venta,
                'Cur. Venta': cur_venta,
                'Comision': '',
                'Cur. Comision': '',
                'Exchange': 'Binance',
                'Grupo': 'Binance',
                'Comentario': comentario,
                'Fecha': line['date']
            }
        )
    return csv_data_processed


def main():
    """
    Imports the data from a csv file, converts it and exports it to another csv file.
    """
    if len(sys.argv) != 3:
        print('This program requires two arguments: source file and target file.')
        exit()

    import_data = import_csv_source_data(sys.argv[1])

    coverted_data = convert_source_to_target_data(import_data)

    export_to_csv_target_data(sys.argv[2], coverted_data)


# start of the application
main()

