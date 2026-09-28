#check if buyer has good credit and give downpayment according to credits
price=1000000
has_good_credits=True
if has_good_credits:
    downpayment= 0.1*price
else:
    downpayment= 0.2*price
print("Downpayment:", downpayment)