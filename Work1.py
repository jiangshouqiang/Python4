var = []
while True:
    num = input("enter a number or Enter:")
    if num:
        try:
             num_str = int(num)
             var.append(num_str)
        except ValueError as es:
         print("None object")
         continue
    else:
        break
sum=0
if len(var) > 0:
    lowest=hightest=var[0]
    for nu in var:
        sum += nu
        if lowest > nu:
            lowest = nu
        if hightest < nu:
            hightest = nu
    print("count="+str(len(var))+" sum="+str(sum)+" lowest= "+str(lowest)+" hightest="+str(hightest)+" mean="+str(sum/len(var)))
else:
    print("no number")



