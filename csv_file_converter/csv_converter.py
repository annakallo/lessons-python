import csv
import os


def import_csv_original_invoices(file_name):
    """
    Imports a csv file with the original invoices and stores it in an array.
    Returns the array.
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + file_name, encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=',')
        csv_data = []
        for line in reader:
            csv_data.append(
                {
                    "cod_fact": line['COD FACT'],
                    "num_fact": line['NUM FACT'],
                    "fecha_fact": line['FECHA FACT'],
                    "id_cliente": line['ID CLIENTE'],
                    "cliente": line['CLIENTE'],
                    "nif_cliente": line['NIF CLIENTE'],
                    "cuenta_pgc": line['CUENTA PGC.'],
                    "ref_orig": line['REF ORIG.'],
                    "base": line['BASE'],
                    "porcentaje_re": line['%R.E'],
                    "re": line['R.E'],
                    "irpf": line['IRPF'],
                    "porcentaje_iva": line['%IVA'],
                    "iva": line['IVA'],
                    "importe": line['IMPORTE'],
                    "es_abono": line['ES ABONO'],
                    "subcuenta": line['SUBCUENTA'],
                    "razon_social": line['RAZON SOCIAL'],
                    "cp": line['CP'],
                    "limite_activo": line['LIMITE ACTIVO'],
                    "no_recibos": line['NO PERMITIR RECIBOS CON FACTURAS VENCIDAS DE MAS DE'],
                    "docum_pago": line['DOCUM.PAGO'],
                    "tipo_pago": line['TIPO PAGO'],
                    "delegacion": line['DELEGACION'],
                }
            )
    return csv_data


def export_to_csv_processed_invoices(export_file_name, csv_data):
    """
    Export a csv file with the data extracted from the original invoices.
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + export_file_name,
              mode='w',
              encoding="utf8") as file:
        fieldnames = ['Nº Factura', 'Fecha', 'Proveedor', 'CIF', 'Base Imponible', 'Cuota IVA', '%IVA',
                      'Ret', '% Ret', 'Rec eq', '% Rec eq', 'Total', 'Tipo gasto']
        writer = csv.DictWriter(file, lineterminator='\n', fieldnames=fieldnames)

        writer.writeheader()
        for line in csv_data:
            writer.writerow({
                'Nº Factura': line['Nº Factura'],
                'Fecha': line['Fecha'],
                'Proveedor': line['Proveedor'],
                'CIF': line['CIF'],
                'Base Imponible': line['Base Imponible'],
                'Cuota IVA': line['Cuota IVA'],
                '%IVA': line['%IVA'],
                'Ret': line['Ret'],
                '% Ret': line['% Ret'],
                'Rec eq': line['Rec eq'],
                '% Rec eq': line['% Rec eq'],
                'Total': line['Total'],
                'Tipo gasto': line['Tipo gasto']
            })


def convert_original_to_processed_data(csv_data_original):
    """
    Converts the data from the original csv to what we want to export.
    """
    csv_data_processed = []
    nr_factura = 1
    for i in range(0, len(csv_data_original)):
        # checking what line we are
        if csv_data_original[i]['cod_fact'] == '':
            continue
        # counting how many types of taxes there are
        base_number = 0
        for line in range(i, len(csv_data_original)):
            if line >= len(csv_data_original) - 1:
                break
            if csv_data_original[line + 1]['cod_fact'] == '':
                base_number += 1
            else:
                break
        # saving the total amount to show it only at the last line of the invoice
        total = csv_data_original[i]['base']
        if base_number == 1:
            total_writen = total
            tipo_gasto = 'Compra dropshipping proveedor'
        else:
            total_writen = ''
            tipo_gasto = ''

        # generating the first line of each invoice
        csv_data_processed.append(
            {
                'Nº Factura': nr_factura,
                'Fecha': csv_data_original[i]['fecha_fact'],
                'Proveedor': 'International Dreamlove S.L.',
                'CIF': 'B90068404',
                'Base Imponible': csv_data_original[i + 1]['base'],
                'Cuota IVA': str(csv_data_original[i + 1]['iva']),
                '%IVA': str(csv_data_original[i + 1]['porcentaje_iva']) + '%',
                'Ret': str(csv_data_original[i + 1]['re']),
                '% Ret': str(csv_data_original[i + 1]['porcentaje_re']) + '%',
                'Rec eq': '0',
                '% Rec eq': '0%',
                'Total': total_writen,
                'Tipo gasto': tipo_gasto
            }
        )
        nr_factura += 1

        # generating the rest of the lines of the invoice if there is more than 1 base
        if base_number > 1:
            for n in range(2, base_number + 1):
                if n == base_number:
                    total_writen = total
                    tipo_gasto = 'Compra dropshipping proveedor'
                else:
                    total_writen = ''
                    tipo_gasto = ''
                csv_data_processed.append(
                    {
                        'Nº Factura': '',
                        'Fecha': '',
                        'Proveedor': 'International Dreamlove S.L.',
                        'CIF': '',
                        'Base Imponible': csv_data_original[i + n]['base'],
                        'Cuota IVA': str(csv_data_original[i + n]['iva']),
                        '%IVA': str(csv_data_original[i + n]['porcentaje_iva']) + '%',
                        'Ret': str(csv_data_original[i + n]['re']),
                        '% Ret': str(csv_data_original[i + n]['porcentaje_re']) + '%',
                        'Rec eq': '0',
                        '% Rec eq': '0%',
                        'Total': total_writen,
                        'Tipo gasto': tipo_gasto
                    }
                )
    return csv_data_processed
