import uuid

def generate_transaction_id():
    return f"TXN-{uuid.uuid4().hex[:8].upper()}"