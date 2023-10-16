import note

class Notes:
    BACKUP_FILENAME = "notes_backup.txt"

    def __init__(self, notes):
        self.notes = notes

    def add_new_note(self, title, content):
        new_note = note.Note(title, content)
        self.notes.append(new_note)

    def check_if_note_exists_in_notes(self, title):
        pass

    def get_note_from_notes(self, title):
        pass

    def edit_note_in_notes(self, title, new_value):
        pass

    def delete_note_from_notes(self, title):
        pass

    def load_notes_from_hard_disc(self):
        pass

    def save_notes_to_hard_disc(self):
        pass
