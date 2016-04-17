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
        'acc_id': ''
    },
    'get_all_by_customer_id': {
        'cust_id': ''
    },
    'get_one': {
        'bill_id': ''
    },
    'update_bill': {
        'bill_id': '',
        'bill': {
            'nickname': 'updated payment'
        }
    },
    'create_bill': {
        'acc_id': '',
        'bill': {
            'status': 'pending',
            'payee': 'Comcast',
            'nickname': 'monthly payment',
            'payment_date': '2015-08-22',
            'recurring_date': 20
        }
    }
}