import urllib

def read_text():
    quotes = open("D:\Curso Python\movie_quotes.txt")
    content= quotes.read()
   
    quotes.close()
    check_profanity(content)
    

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output= connection.read()
    
    connection.close()
    if(output=="true"):
        print("Profanity Alert!!!!!!!!!!")
    else:
        print("The text has no curse words")
    
read_text()  
