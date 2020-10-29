filename = ('E:\BINUS\Every meeting file\File CompSci\week 6\Assignment Week 6\AVB.txt')
def txtfile ():
    with open (filename, 'r') as f:
        a = f.read()
        b = a.split("\n")
        c = open(filename, 'w') 
        i = 0     
        while i < len(b):
            b[i] = str(i) +" " + b[i] +"\n"
            c.write(b[i])
            i+=1
        print(filename)
txtfile () 