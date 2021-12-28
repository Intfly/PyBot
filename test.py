vect_s2= [{'oui':1},{'non':2}]
f= open("guru99.py","w+")
for i in vect_s2:
    for k,v in i.items():
        if v ==1:
            f.write(f"oui   {k}    {v}")
