

def get_quant_count(request):
    quantsum=0
    cart = request.session.get('cart', {})
    for item_quantity in cart.items():
     quantsum+=item_quantity[1]
    return{ 'quantsum':quantsum }
    
