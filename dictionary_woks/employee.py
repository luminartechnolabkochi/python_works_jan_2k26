"""
create a dictionary of product with attribute 
id,title,price,avl_qty
"""


product = {"id":12,"title":"oreo","price":45,"avl_qty":50}


print(product["title"])

product["avl_qty"]+=10
print(product)
# code:sku12

product["code"]="sku12"

print(product)

# chk key exist or not

if "offer" in product:

    print("yes")

else:

    print("no")