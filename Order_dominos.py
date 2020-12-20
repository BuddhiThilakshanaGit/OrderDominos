import pizzapi

customer = Customer('Fname', 'Lname', 'email', 'mobilephone', 'adress')
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
# menu = my_local_dominos.get_menu() #can view the menu of dominos
order = Order.begin_customer_order(customer, my_local_dominos)
order.add_item('P12IPAZA') # add a 12-inch pan pizza
order.add_item('MARINARA') # with an extra marinara cup
order.add_item('20BCOKE')  # and a 20oz bottle of coke
card = CreditCard('4100123422343234', '0115', '777', '90210')

#finally checkout and place the order
order.place(card)
my_local_dominos.place_order(order, card)
