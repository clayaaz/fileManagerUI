from funtion import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("720x720")
root.maxsize(720, 720)

docCh = customtkinter.BooleanVar(value=True)
imgCh = customtkinter.BooleanVar(value=True)
audCh = customtkinter.BooleanVar(value=True)
vidCh = customtkinter.BooleanVar(value=True)
cdCh = customtkinter.BooleanVar(value=True)
scCh = customtkinter.BooleanVar(value=True)


def createFolder():
    if docCh.get():
        os.mkdir(loc + doc)
    if imgCh.get():
        os.mkdir(loc + img)
    if audCh.get() == True:
        os.mkdir(loc + aud)
    if vidCh.get() == True:
        os.mkdir(loc + vid)
    if cdCh.get() == True:
        os.mkdir(loc + cd)
    if scCh.get() == True:
        os.mkdir(loc + sc)


label = customtkinter.CTkLabel(master=root, text="File Manager", font=("Roboto", 24))
label.pack(pady=12, padx=10)

frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(pady=10, padx=30, fill="both", expand=False)

usrname = customtkinter.CTkEntry(
    master=frame2, placeholder_text="Your Windows Username"
)
usrname.pack(pady=12, padx=10)


def setUsr():
    loc = f"c:\\Users\\{usrname.get()}\\Desktop\\"


setusr = customtkinter.CTkButton(master=frame2, text="Set Username", command=setUsr)
setusr.pack(pady=12, padx=10)

frame3 = customtkinter.CTkFrame(master=root)
frame3.pack(pady=10, padx=30, fill="both", expand=False)


button = customtkinter.CTkButton(master=frame2, text="Manage File", command=mainFunc)
button.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(
    master=frame3, text="What Folders Do You Want to Create?", font=("Roboto", 24)
)
label2.pack(pady=12, padx=10)

checkboxDoc = customtkinter.CTkCheckBox(
    master=frame3, text="Document", variable=docCh, onvalue=True, offvalue=False
)
checkboxDoc.pack(pady=12, padx=10)

checkboxImg = customtkinter.CTkCheckBox(
    master=frame3, text="Images", variable=imgCh, onvalue=True, offvalue=False
)
checkboxImg.pack(pady=12, padx=10)

checkboxAud = customtkinter.CTkCheckBox(
    master=frame3, text="Audio", variable=audCh, onvalue=True, offvalue=False
)
checkboxAud.pack(pady=12, padx=10)

checkboxVid = customtkinter.CTkCheckBox(
    master=frame3, text="Video", variable=vidCh, onvalue=True, offvalue=False
)
checkboxVid.pack(pady=12, padx=10)

checkboxCd = customtkinter.CTkCheckBox(
    master=frame3, text="Code Files", variable=cdCh, onvalue=True, offvalue=False
)
checkboxCd.pack(pady=12, padx=10)

checkboxSc = customtkinter.CTkCheckBox(
    master=frame3, text="Applications", variable=scCh, onvalue=True, offvalue=False
)
checkboxSc.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(
    master=frame3, text="Create Folder", command=createFolder
)
button2.pack(pady=12, padx=10)


root.mainloop()
