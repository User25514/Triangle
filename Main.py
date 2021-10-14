a = [" "]*50
a[int((len(a)+1)/2)-1] = "."
for x in range(0,int(len(a)/2)):
    print("".join(a))
    a[int((((len(a)+1)/2))+x)] = a[int((((len(a)-1)/2)-1)-x)] = a[int((len(a)+1)/2)-1] = "."
