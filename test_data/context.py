account = {
    'get_all_by_type': {
        'acc_type': 'Credit Card'
    },
    'get_one': {
        'acc_id': '56c66be7a73e492741508102'
    },
    'get_all_by_customer_id': {
        'cust_id': '56c66be6a73e4927415074ca'
    },
    'update_account': {
        'acc_id': '56c66be7a73e492741508102',
        'request_data': {
            'nickname': 'Brand New Test Update'
        }
    },
    'create_account': {
        'cust_id': '56c66be6a73e4927415074ca',
        'request_data': {
            'type': 'Credit Card',
            'nickname': 'Brand New Test Account',
            'rewards': 0,
            'balance': 0
        }
    }
}

atm = {
    'get_all_by_location': {
        'lat': 38.882163,
        'lng': -77.1113105,
        'rad': 1
    },
    'get_one': {
        'id': '56c66be5a73e492741506f30'
    }
}

bill = {
    'get_all_by_account_id': {
        'acc_id': '56c66be7a73e492741508102'
    },
    'get_all_by_customer_id': {
        'cust_id': '56c66be6a73e4927415074ca'
    },
    'get_one': {
        'bill_id': '56c66be8a73e492741508d48'
    },
    'update_bill': {
        'bill_id': '56c66be8a73e492741508d48',
        'bill': {
          'status': 'pending',
          'payee': 'Updated Payee',
          'nickname': 'Andrews Awesome Test Class',
          'payment_date': '2016-04-17',
          'recurring_date': 1
        }
    },
    'create_bill': {
        'acc_id': '56c66be7a73e492741508102',
        'bill': {
            'status': 'pending',
            'payee': 'Comcast',
            'nickname': 'monthly payment',
            'payment_date': '2015-08-22',
            'recurring_date': 20
        }
    }
}