import mechanicalsoup
import sys


# create stateful browser
brow = mechanicalsoup.StatefulBrowser()

shipping_ids = ["checkout_email" ,"checkout_shipping_address_first_name", "checkout_shipping_address_last_name", "checkout_shipping_address_address1", "checkout_shipping_address_address2",
									"checkout_shipping_address_city", "checkout_shipping_address_province", "checkout_shipping_address_zip", "checkout_shipping_address_phone" ]

# soup.py "accessories" "cap" "bobob@bob.com" "bob" "BOBOB" "68 Road Lane" "" "Troy" "New York" "12180" "1234567789"

product = sys.argv[1:3]
shipping_values = sys.argv[3:]

# shipping_values = ["bobob@bob.com","bob", "BOBOB", "68 Road Lane", "", "Troy", "New York", "12180", "1234567789"]

#set proxy/proxies
proxies={'http': 'my proxy',}
brow.session.proxies = proxies

# When using variants import variant link here
# # use brow to open link
# brow.open("https://shopnicekicks.com/cart/10638898049:1")
# # check url
# print(brow.get_url())


# use brow to open link
brow.open("https://kith.com")

# search current page for new page links
for link in brow.links(url_regex=product[0]):
	r = brow.follow_link(link)
	print(brow.get_url())
	break

# search current page for new page links
for link in brow.links(url_regex=product[1]):
	r = brow.follow_link(link)
	print(brow.get_url())
	break

# select form
f = brow.select_form(nr=2)

# submit form (add to cart)
brow.submit_selected()
# # check url
print(brow.get_url())



# select form
f = brow.select_form(nr=2)
# submit form (go to checkout page)
brow.submit_selected("checkout")
# # check url
print(brow.get_url())



# select form
f = brow.select_form(nr=0)



for i in range(len(shipping_ids)):
	brow.get_current_form().form.select('input[id="'+ shipping_ids[i] +'"]')[0]['value'] = shipping_values[i]


# submit form (shipping information page)
brow.submit_selected()
# check url
print(brow.get_url())

# navigate to checkout page
brow.select_form(nr=0)
brow.submit_selected()
print(brow.get_url())

#
# # brow.select_form(nr=2)
# # # brow.get_current_form().print_summary()
