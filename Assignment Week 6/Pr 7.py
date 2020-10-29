filename = ('E:\BINUS\Every meeting file\File CompSci\week 6\Assignment Week 6\NEWEBOOK.txt')
def avrgWord():
    with open (filename,'r') as f :
        text = f.read().replace("\n"," ")
        countword = 0 
        countword2 = 0 
        countword = len(text)   
        newtext = ""
        for i in text :
            newtext += i

        text = newtext
        txtsplit = text.split(" ") 
        for word in txtsplit:
            countword2 += 1

        avrg = countword/countword2
        print ("The avrg word len of the text file", filename, "is: ", avrg) 

avrgWord()