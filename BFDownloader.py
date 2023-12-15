import os

#Format Files
def format(name):
    #Reformat Files
    lines = []

    files = os.listdir(".")
    for i in range(len(files)):
        filename = files[i]
        if filename.endswith(".mp3"):
            trackname = "track" + str(i) + ".mp3"
            os.rename(files[i], trackname)
            lines.append("file " + trackname + " \n")
    lines[-1] == lines[-1].replace("\n", "")

    #Write input.txt
    txtfile = open("input.txt", "w")
    txtfile.writelines(lines)
    txtfile.close()

    #FFMPEG Concat and Reformat
    os.system("ffmpeg -f concat -i input.txt concat.mp3")
    os.system("ffmpeg -i track0.mp3 -i concat.mp3 -map 1 -c copy -map_metadata 0 -map_metadata:s:v 0:s:v -map_metadata:s:a 0:s:a metaconcat.mp3")
    os.system(f'ffmpeg -i metaconcat.mp3 -metadata title="{name}" -c copy "{name}.mp3"')

    #Delete Files
    for filename in os.listdir("."):
        if filename != f"{name}.mp3" and not filename.endswith(".py"):
            os.remove(filename)


#Take Input
playlists = []
inputing = True
while inputing:
    entry=  []
    url = input("Playlist URL (n to stop): ")
    if url != "n":
        entry.append(url)
        entry.append(input("Enter Name: "))
        playlists.append(entry)
    else:
        inputing= False

#Loop Through Requests
for item in playlists:
    os.system(f"zspotify -pl {item[0]}")
    os.chdir(f"{os.path.expanduser('~')}\Music\ZSpotify Music\{item[1]}")
    format(item[1])

#Confirmation Output
print("\nSuccessfully Completed\n")