from ecommerce.shopping.sales import calc_shipping, calc_tax
from ecommerce.shopping import sales
import ecommerce.shopping.sales
import sys
# from ..customer import contact
from ecommerce.customer import contact
contact.contact_customer()
calc_shipping()
calc_tax()

ecommerce.shopping.sales.calc_tax()
ecommerce.shopping.sales.calc_shipping()
# print(sys.path)
# print(dir(sales))
print(sales.__name__)
print(sales.__file__)
print(sales.__package__)
print(sales.__doc__)
