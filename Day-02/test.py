arn = "arn:aws:iam::123456789012:user/Development/product_1234/mahesh"

arn_output = (arn.split("/")[3])

print(arn_output)