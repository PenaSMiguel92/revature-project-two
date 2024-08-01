

def row_generator(cur_row: int, customer: dict, transaction: dict, product: dict, **kwargs) -> list[str]:
    """
        This method takes in dictionaries and generates a row to be written to csv file.
        
        Set errorize to True: errorize=True to randomly add in an error to the row.
        ;param; cur_row: int, customer: dict, transaction: dict, product: dict, **kwargs
        ;returns; str <- string combining columns
    """
    row_list = []
    row_list.append(str(cur_row))
    row_list.append(customer.get('id'))
    row_list.append(customer.get('full_name'))
    row_list.append(product.get('product_id'))
    row_list.append(product.get('name'))
    row_list.append(product.get('category'))
    row_list.append(transaction.get('payment_type'))
    row_list.append(product.get('quantity'))
    row_list.append(product.get('price'))
    row_list.append(transaction.get('datetime'))
    row_list.append(customer.get('country'))
    row_list.append(customer.get('city'))
    row_list.append(product.get('website'))
    row_list.append(transaction.get('payment_tx_id'))
    row_list.append(transaction.get('payment_tx_success'))
    row_list.append(transaction.get('failure_reason'))
    return row_list

