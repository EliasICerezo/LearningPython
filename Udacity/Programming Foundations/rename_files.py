import os

def rename_files():
    #Obtener ficheros
    file_list = os.listdir(r"D:\Descargas\prank")
    print(file_list)
    saved_path=os.getcwd()
    
    os.chdir(r"D:\Descargas\prank")
    #Renombrar ficheros
    for file_name in file_list:
        oldfn=file_name
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print(oldfn+"->"+file_name)

    os.chdir(saved_path)


    
rename_files()
    
