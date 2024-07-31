# Import Functions
from utils.data_generators  import customer_details, transaction_details 
import csv

def main():

    # Generate a customer
    """ 
    Returns 
    {   'id': 1, 
        'full_name': 'Thomas Edison', 
        'city': 'San Francisco', 
        'country': 'United States'
    }
    """
    customer = customer_details() 

    # Generate a transaction
    """
    Returns
    {   'datetime': formatted_datetime,
        'payment_type': payment_type,
        'payment_tx_id': payment_tx_id,
        'payment_tx_success': payment_tx_success,
        'failure_reason': failure_reason
    }
    """
    transaction = transaction_details()
    
    
    # Combine the Return Types to Generate the CSV
    # Include the error function
    #Testing branching.
    return