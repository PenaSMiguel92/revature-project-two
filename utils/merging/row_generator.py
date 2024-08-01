

def row_generator(cur_row: int, customer: dict, transaction: dict, product: dict, **kwargs) -> str:
    """
        This method takes in dictionaries and generates a row to be written to csv file.
        
        Set errorize to True: errorize=True to randomly add in an error to the row.
        ;param; cur_row: int, customer: dict, transaction: dict, product: dict, **kwargs
        ;returns; str <- string combining columns
    """
    result_list = []
    result_str += f'{cur_row},{customer.get('id'),{customer.get('full_name')}},{product.get('product_id')},'
    result_str += f'{product.get('name')},{product.get('category')},{transaction.get('payment_type')},'
    result_str += f'{product.get('quantity')},{product.get('price')},{transaction.get('datetime')},'
    result_str += f'{customer.get('country')},{customer.get('city')},{product.get('website')},'
    result_str += f'{transaction.get('payment_tx_id'),{transaction.get('payment_tx_success')},{transaction.get('failure_reason')}}'
    return result_str

