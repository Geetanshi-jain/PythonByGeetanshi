import os
if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")

    #renamemehtod
    #os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}",)

    folders =os.listdir("data")
    print(folders)
    os.cwd()

    