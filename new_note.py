import gi
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class NewNoteWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="New Note")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box)

        self.entry_title = Gtk.Entry()
        self.entry_title.set_text("Title")
        box.pack_start(self.entry_title, True, True, 0)

        self.entry_text = Gtk.Entry()
        self.entry_text.set_text("Note")
        box.pack_start(self.entry_text, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Save")
        button.connect("clicked", self._save)
        box.pack_start(button, True, True, 0)

    def _save(self,x):
        i = 0
        print("Saving")
        with open('notes.json') as data_file:
            data = json.load(data_file)
        notes = data["notes"]
        print(notes)

        for note in notes:
            print(note)
            i = note["note-id"]

        next_id = i + 1
        note_title = self.entry_title.get_text()
        note_text = self.entry_text.get_text()
        note_cat = "XXX"

        new_dict = {'note-id':next_id, 'note-title': note_title, 'note-text':note_text,'note-category':note_cat}
        new_list = notes+ [new_dict]
        new_json = "{\"notes\":" +json.dumps(new_list)+ "}"
        print(new_json)
        with open('notes.json', 'r+') as data_file:
            data_file.seek(0)
            data_file.write(new_json)
            data_file.truncate()

        self.destroy()  
