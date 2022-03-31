import easygui as eg
import pywhatkit as kt
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def importFile():
    
    extension = ["*.png","*.jpg"]

    try:
    
        e_file = eg.fileopenbox(msg="Select an input file PNG or JPG",
                         title="Control: fileopenbox",
                         default="",
                         filetypes=extension,
                         multiple=False)

        root, extension = os.path.splitext(e_file)

        if extension == ".png" or extension == ".png" :
            return e_file
        
        else:
            eg.exceptionbox("File must be an JPG or PNG", "Error")
            importFile()
    except:
        raise Exception("File Open Failed")

def locateOutput(extension = "txt"):
    # If user cancels it defaults to the FIRST choice. We want default to be NO so I reverse the default of choices here. 
        saveornot = eg.buttonbox(msg="Do you want to save results to a file?", choices = ("No", "Yes") )
        if saveornot == "Yes":
            filename = eg.filesavebox(msg = "Where do you want to save the file (extension %s will automatically be added)?" %(extension))
            if filename is None:
                return None
            #
            if os.path.exists(filename):
                ok_to_overwrite = eg.buttonbox(msg="File %s already exists. Overwrite?" %(filename), choices = ("No", "Yes") )
                if ok_to_overwrite == "Yes":
                    return filename
                else:
                    return None
            else:
                return filename
        else:
            return None

def convertFile(initial_file,f_location):
    
    try:

        c_file = kt.image_to_ascii_art(initial_file, str(f_location))

        return c_file

    except:
        eg.exceptionbox("Server Error: 500 Failed to convert", "Error")
        anotherFile()

def anotherFile():
    
    tryAgain = eg.buttonbox(msg="Do you want to convert another file?", choices = ("No", "Yes") )
        
    if tryAgain == "Yes":
        main()
    else: 
        exit()


def main():
    
    f_in = importFile()
    f_location = locateOutput()
    
    if f_location != None:
        ascii_file = convertFile(f_in, f_location)
    else:
        anotherFile()

    anotherFile()

if __name__ == "__main__":
    eg.msgbox(msg='This software was made for educational purposes. Use by your own risk - Enjoy!',
          title='Welcome to PNG/JPG to ascii converter ', 
          ok_button='Continue',
          image="./assets/img/Python.png")
    main()