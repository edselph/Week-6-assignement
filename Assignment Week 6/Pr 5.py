import string
filename = ('E:\BINUS\Every meeting file\File CompSci\week 6\Assignment Week 6\EBOOK.txt')
def hapaxes() : 
    with open (filename, 'r') as f :
        text = f.read().lower().replace('\n',"")
        newtext = ""
        
        for i in text :
            if i not in string.punctuation :
                newtext += i
        text = newtext

        txtsplit = text.split(" ") 
        
        display = {} 
        for i in txtsplit :
            if i not in display:
                display[i] = 1 
            else :
                display[i] += 1

        newdisplay = [] 
        for i in display:
            if display[i] == 1:
                newdisplay.append(i)
        
        print('hapaxes found in text: ')
        for word in newdisplay:
            print(word)
        
hapaxes()
