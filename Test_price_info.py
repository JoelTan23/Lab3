import price_info as price_info

def test_total_cost():
      
    result = price_info.total_cost_shopping()
	
    assert (result == 6) # still need to work on this
	
def test_price():
	
    result = price_info.cost_of_fruits("apple",10) 
    
    assert (result == 12.0)