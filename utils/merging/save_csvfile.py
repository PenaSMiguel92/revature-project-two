import csv


def save_data(rows_to_write: list[list[str]]) -> bool:
    """
        This function takes in a list of list of strings.

        csv.writer.writerows joins each list of strings as comma seperated values.

        This function returns a boolean when saving data to .csv file is complete
    """
    filename = 'data/ouput.csv'
    with open(filename, 'w+', newline='') as output_file: 
        #note that newline='' is for windows. since it does something like \n\n
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(rows_to_write)

    return True