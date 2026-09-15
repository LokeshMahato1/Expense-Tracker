class Expenses:
    def __init__(self,
                 category,
                 amount,
                 description,
                 method,
                 txn_id,
                 date
                 ):

        self.category=category
        self.amount=amount
        self.description=description
        self.method=method
        self.txn_id=txn_id
        self.date=date
        