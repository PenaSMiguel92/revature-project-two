# Import Functions
from utils.csv_generators import customer_details, transaction_details, product_purchase_details
from utils.merging import row_generator, save_csvfile

def main():
    rows_to_write = []
    for row_id in range(12000):
        # Generate a customer
        """ 
        Returns 
        {   
            'id': 1, 
            'full_name': 'Thomas Edison', 
            'city': 'San Francisco', 
            'country': 'United States'
        }
        """
        customer = customer_details.customer_details() 

        # Generate a transaction
        """
        Returns
        {   
            'datetime': formatted_datetime,
            'payment_type': payment_type,
            'payment_tx_id': payment_tx_id,
            'payment_tx_success': payment_tx_success,
            'failure_reason': failure_reason
        }
        """
        transaction = transaction_details.transaction_details()
        
        # Generate a product
        """
        Returns
        {   'product_id': 8,
            'category': 'meds',
            'name': 'diet pills',
            'price': 58.49,
            'website': 'chewy.com'
            'quantity': 2
        }
        """
        product = product_purchase_details.product_purchase_details()
        
        row_to_write = row_generator.row_generator(row_id, customer, transaction, product, errorize=True)
        rows_to_write.append(row_to_write)
    
    save_csvfile.save_data(rows_to_write)
        # Combine the Return Types to Generate the CSV
        # Include the error function
        #Testing branching.
    
    return