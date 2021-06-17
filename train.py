import webbrowser
from zipfile import ZipFile
import os
import time

def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths  

def train(args):
    files_to_zip = []
  
    # calling function to get all file paths in the directory
    images_paths = get_all_file_paths(args.dataset_path)

    #zipping images
    with ZipFile('obj.zip', 'w') as zip:
        for f in images_paths:
            zip.write(f,arcname=f[f.index('/')+1:])

    #zipping other files
    with ZipFile('Training_Pack.zip', 'w') as zip:
        zip.write(args.yolo_cfg_file,arcname='obj.cfg')
        zip.write(args.yolo_data_file,arcname='obj.data')
        zip.write(args.yolo_names_file,arcname='obj.names')
        zip.write("generate_train.py")
        zip.write(args.yolo_weights_file,arcname='obj.weights')
        zip.write("obj.zip")

    os.remove('obj.zip')

    input("Created zip file: %s \n Upload it to your google drive and press enter to continue" %(os.path.abspath('Training_Pack.zip')))
    webbrowser.open_new("https://colab.research.google.com/drive/1Y2ZeFsSL0E_wd6a3-AYArqQA9ONpXP2K?usp=sharing")

