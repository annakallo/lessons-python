from csv_file_converter import csv_converter


def main():
    """
    Imports the data from a csv file, converts it and exports it to another csv file.
    """
    print('The directory contains the facturas-iva-desglosado.csv, you can import this file to be converted or add '
          'another csv file to the directory and import that.')
    import_file_name = input('Enter the import filename: ')
    # print('You entered: ' + import_file_name)
    export_file_name = input('Name the newly created export file: ')
    # print('You entered: ' + export_file_name)

    import_data = csv_converter.import_csv_original_invoices(import_file_name)

    coverted_data = csv_converter.convert_original_to_processed_data(import_data)
    for line in coverted_data:
        print(line)

    csv_converter.export_to_csv_processed_invoices(export_file_name, coverted_data)


# start of the application
if __name__ == '__main__':
    main()

