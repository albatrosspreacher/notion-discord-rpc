from subprocess import Popen, PIPE
from pypresence import Presence
import time

(var3, tError) = Popen(['osascript', 'Setup.scpt'], stdout=PIPE, universal_newlines=True).communicate()
title = var3.strip()

"""
You need to upload your image(s) here:
https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
"""

client_id = "861651444234846258"  # application ID
RPC = Presence(client_id=client_id)
RPC.connect()

# use the same name that you used when uploading the image
RPC.update(large_image="notion_1024", large_text="Notion",
            small_image="keeb_512", small_text="Organizing my life!", start=int(time.time()), details=("Editing: " + title))

while 1:
    time.sleep(15) #Can only update presence every 15 seconds