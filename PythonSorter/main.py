import random
import string
import os
from termcolor import colored
from FileTypeSorter import FileFoldermap as mapFile

# FILE_EXTENSIONS
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "FONTS": [".otf", ".woff", "woff2", "ttf"]
}

# FORMAT FILE_EXTENSIONS TO DIRECTORY NAME
FILE_FORMATS = {file_format: directory
for directory, file_formats in DIRECTORIES.items()
for file_format in file_formats}

CharList = string.ascii_letters + string.digits
SortTheseFiles = os.listdir()

for file in SortTheseFiles :
    filename, file_extension = os.path.splitext(file)
    if file_extension in FILE_FORMATS :
        folder = FILE_FORMATS[file_extension]
        mapFile(file, folder)
    else :
        continue