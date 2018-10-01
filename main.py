import gi
import json
import new_note
import view_note

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk
from gi.repository import AppIndicator3


def build_menu(n):
    menu = Gtk.Menu()
    menu_list = Gtk.Menu()
    for note in n:
        print(note)
        # print(note_data)
        list_item = Gtk.MenuItem(note["note-title"])
        list_item.connect('activate', view_n, note["note-id"])
        menu_list.append(list_item)

    item_list = Gtk.MenuItem('All Notes')
    item_list.set_submenu(menu_list)
    menu.append(item_list)

    item_new = Gtk.MenuItem('New Note')
    item_new.connect('activate', new_n)
    menu.append(item_new)

    menu.show_all()
    return menu


def new_n(__):
    print("new note")
    win = new_note.NewNoteWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def view_n(x, nid):
    print(id)
    win = view_note.NewNoteWindow(nid)
    win.resize(600,600)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    app_id = "MAKE_A_NOTE"
    app_icon = "emblem-nowrite"
    cat = AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    ind = AppIndicator3.Indicator.new(app_id, app_icon, cat)

    with open('notes.json') as data_file:
        data = json.load(data_file)
    notes = data["notes"]

    ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    ind.set_menu(build_menu(notes))
    Gtk.main()
