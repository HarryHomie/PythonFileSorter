import os, shutil

path = r"C:/Users/harry/Downloads/"
file_name = os.listdir(path)

foldernames=["disks", "images", "word files","Torrent"]
total_folders= len(foldernames)

for i in range(total_folders):
    if not os.path.exists(path+foldernames[i]):
        print("Made a directory")
        os.mkdir(path+foldernames[i])

for file in file_name:
    if file.endswith(".iso") and not os.path.exists(path+"disks/"+file):
        shutil.move(path + file, path+"disks/"+file)
    
    elif file.endswith(".torrent") and not os.path.exists(path+"Torrent/"+file):
        shutil.move(path + file, path+"Torrent/"+file)
        
    elif file.endswith(".jpeg") or file.endswith(".png") and not os.path.exists(path+"images/"+file):
        shutil.move(path + file, path+"images/"+file)
        
    elif file.endswith(".doc") or file.endswith(".txt") or file.endswith(".docx") and not os.path.exists(path+"word files/"+file):
        shutil.move(path + file, path+"word files/"+file)
        
    else:
        print("Nothing was done to this file")