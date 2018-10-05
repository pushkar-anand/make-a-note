import gi
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class NewNoteWindow(Gtk.Window):
    def __init__(self, nid):
        Gtk.Window.__init__(self, title="Note")

        with open('notes.json') as data_file:
            data = json.load(data_file)
        notes = data["notes"]

        #Looping through all the notes to check which note is being viewed
        for note in notes:
            print(note)
            if note["note-id"] == nid:
                self.title = note["note-title"]
                self.note_text = note["note-text"]
                self.cat = note["note-category"]
                break

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        self.add(box)

        self.label = Gtk.Label()
        self.label.set_markup("<big><b>"+self.title+"</b></big>")
        box.pack_start(self.label, True, True, 0)

        self.label = Gtk.Label(self.note_text)
        self.label.set_line_wrap(True)
        self.label.set_justify(Gtk.Justification.FILL)
        box.pack_start(self.label, True, True, 0)
