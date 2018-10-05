# make-a-note
An application built over Gimp Toolkit(GTK) to remove to ease the note making process. It has over-the-top functionality, which enables the user to take quick notes. Simply start this app and use the icon in the status bar to add and view notes.

# Running instructions

Download/Clone the repository.

Install Gimp-Toolkit(if required): `sudo apt-get install python3 gtk+3 python3-gobject`.

Install gi:
`sudo apt install python-gi python-gi-cairo python3-gi`

Run the script:
`python main.py`

## As a startup service:
To run this app at start use cron:

`sudo crontab -e`

Scroll to the bottom of the page and add the following line (after all the #'s):

`@reboot python /path/to/main.py &`

# Screenshots
## Taking new notes:
![Screenshot 1](https://raw.githubusercontent.com/pushkar-anand/make-a-note/master/screenshots/1.png)
## Viewing the notes
![Screenshot 2](https://raw.githubusercontent.com/pushkar-anand/make-a-note/master/screenshots/2.png)