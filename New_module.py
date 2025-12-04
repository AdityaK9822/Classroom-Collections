def math_operations(a, b, operator):
    if operator == "+":
        print("Sum is ", float(a)+float(b))
    elif operator == "-":
        print("Difference is ", float(a)-float(b))
    elif operator == "*":
        print("Product is ", float(a)*float(b))
    elif operator == "/":
        print("Quotient is ", float(a)/float(b))
    elif operator == "square":
        print("Square is ", float(a)**2)
    elif operator == "check":
        if a%2==0:
            print("Number is even")
        else:
            print("Number is odd")