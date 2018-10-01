# make-a-note
This gtk application helps you save some important things without having to switch to a different app. Simply start this app and use the icon in the status bar to add and view notes.

# running instructions

simply clone/download the repo and run the note.py script:

`python main.py`

to auto start the script at startup
use cron:

`sudo crontab -e`

Scroll to the bottom and add the following line (after all the #'s):

`@reboot python /path/to/main.py &`

