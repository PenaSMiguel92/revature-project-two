# Write a function that returns a list dictionary of 3 values
#  random date between 1/1/2020 and 12/31/2020
#  payment_type
#  payment_tx_id
#  payment_tx_success (99%+ positive, rarely negative)
#  failure_reason (is null unless payment_tx_success is false, other wise select a reason from list of failures.)
from datetime import datetime, timedelta
import random


def transaction_details():
    # Define the start and end dates
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 3)

    # Calculate the total number of seconds between the start and end dates
    total_seconds = int((end_date - start_date).total_seconds())

    # Generate a random number of seconds within this range
    random_seconds = random.randint(0, total_seconds)

    # Add the random number of seconds to the start date to get the random date
    random_datetime = start_date + timedelta(seconds=random_seconds)
    # Format the random datetime to the desired format
    formatted_datetime = random_datetime.strftime("%Y-%m-%d %H:%M:%S")
    payment_type = random.choice(['credit_card', 'paypal', 'apple_pay', 'google_pay'])
    payment_tx_id = random.randint(1000000000, 9999999999)
    payment_tx_success = random.choices([True, False], [0.99, 0.01])[0]
    failure_reason = None
    if not payment_tx_success:
        failure_reason = random.choice(['insufficient funds', 'network error', 'unable to verify identity'])
    return {
        'datetime': formatted_datetime,
        'payment_type': payment_type,
        'payment_tx_id': payment_tx_id,
        'payment_tx_success': payment_tx_success,
        'failure_reason': failure_reason
    }

