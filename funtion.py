import os
import shutil

# the directory location
loc = "c:\\Users\\shrey\\OneDrive\\Desktop\\"

# listens to the fils in the direcory
dir = os.listdir(loc)

# list of extentions
document_file_extensions = [
    ".doc",
    ".docx",
    ".odt",
    ".rtf",
    ".txt",
    ".pdf",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".csv",
    ".md",
    ".tex",
]
image_file_extensions = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
    ".svg",
    ".ico",
    ".psd",
    ".ai",
    ".eps",
]
audio_file_extensions = [
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",
    ".aac",
    ".m4a",
    ".wma",
    ".aiff",
    ".alac",
    ".mid",
    ".midi",
]
code_file_extensions = [
    ".c",
    ".cpp",
    ".java",
    ".js",
    ".html",
    ".css",
    ".php",
    ".rb",
    ".swift",
    ".go",
    ".lua",
    ".pl",
    ".sql",
    ".sh",
    ".json",
    ".xml",
    ".yml",
    ".yaml",
]
video_file_extensions = [
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".mpeg",
    ".mpg",
    ".m4v",
    ".3gp",
    ".m2ts",
    ".mts",
    ".vob",
    ".ts",
    ".asf",
    ".rm",
    ".rmvb",
    ".ogv",
    ".divx",
]


doc = "Documents"
img = "Images"
aud = "Audio"
vid = "Videos"
cd = "Code"
sc = "Shortcuts"


# funtion to check file extention
def checkExt(file):
    file_extention = os.path.splitext(file)
    return file_extention[1]


# main loop
def mainFunc():
    for x in dir:
        fileExt = checkExt(x)
        print(x)
        for d in document_file_extensions:
            if fileExt == d:
                shutil.move(loc + x, loc + doc)
            else:
                pass
        for i in image_file_extensions:
            if fileExt == i:
                shutil.move(loc + x, loc + img)
            else:
                pass
        for a in audio_file_extensions:
            if fileExt == a:
                shutil.move(loc + x, loc + aud)
            else:
                pass
        for c in code_file_extensions:
            if fileExt == c:
                shutil.move(loc + x, loc + cd)
            else:
                pass
        for v in video_file_extensions:
            if fileExt == v:
                shutil.move(loc + x, loc + vid)
            else:
                pass

        if fileExt == ".lnk" or fileExt == ".url" or fileExt == ".exe":
            shutil.move(loc + x, loc + sc)
        else:
            pass
        pass
