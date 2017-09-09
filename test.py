import json
if __name__ == '__main__':

    with open('notes.json') as data_file:
        data = json.load(data_file)
    notes = data["notes"]
    print(notes)
    #notes_data = json.loads(notes[0])
    print(notes[0])
