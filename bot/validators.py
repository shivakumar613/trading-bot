def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()

def validate_quantity(quantity):
    q = float(quantity)
    if q <= 0:
        raise ValueError("Quantity must be positive")
    return q

def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT orders")
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be positive")
        return p
    return None