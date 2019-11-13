import os, shutil, string, random
import time, datetime

class FileFoldermap :
    direct_name = 'DIRECTORY'
    working_directory = os.getcwd()

    def renameFiles(self, file, foldern) :
        letters = string.ascii_letters + string.digits
        name = ''
        name += ''.join(random.choice(letters) for i in range(1, 12))
        file_name, file_extension = os.path.splitext(file)
        Files_in_folder = os.listdir(self.direct_name + "/" + foldern)
        for file in Files_in_folder :
            compare_file, compare_file_extension = os.path.splitext(file)
            if compare_file == file_name :
                os.rename(self.direct_name + "/" + foldern + "/" + file_name + file_extension, self.direct_name + "/" + foldern + "/" + name + compare_file_extension)
            else :
                continue

    def report(self, this) :
        rPath = self.working_directory + "\\" + this
        print("New folder created at:(" + rPath + ")")


    def __init__(self, file, foldern) :
        folder_path1 = self.direct_name + "/" + foldern
        folder_path2 = self.direct_name + "\\" + foldern
        if not os.path.isdir(self.direct_name) :
            os.mkdir(self.direct_name)
            self.report(self.direct_name)
            time.sleep(.5)
        if not os.path.isdir(folder_path1) :
            os.mkdir(folder_path1)
            self.report(folder_path2)
            time.sleep(.5)
        self.renameFiles(file, foldern)
        shutil.move(file, folder_path1 + "/" + file)
        
        
        
