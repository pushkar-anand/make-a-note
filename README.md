# make-a-note
An application built over Gimp Toolkit(GTK) to remove to ease the note making process. It has over-the-top functionality, which enables the user to take quick notes. Simply start this app and use the icon in the status bar to add and view notes.

# Running instructions

simply clone/download the repo and run the note.py script:

`python main.py`

to auto start the script at startup
use cron:

`sudo crontab -e`

Scroll to the bottom and add the following line (after all the #'s):

`@reboot python /path/to/main.py &`

# Screenshots
![Screenshot 1](https://raw.githubusercontent.com/pushkar-anand/make-a-note/master/screenshots/1.png)
![Screenshot 2](https://raw.githubusercontent.com/pushkar-anand/make-a-note/master/screenshots/2.png)
