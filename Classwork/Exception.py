i=-1
if i<0:
    raise NameError("Name error")
    raise Exception("Exception")
#Both NameError and Exception are don't work together in one condition
x = None
if x is None:
    raise NameError("Value error")