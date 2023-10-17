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
        for note in self.notes:
            if note.title == title:
                note.edit_note(title, new_value)
                print(f"Notatka '{title}' została zaktualizowana.")
                break
        else:
            print(f"Nie znaleziono notatki '{title}'.")

    def delete_note_from_notes(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f"Notatka '{title}' została usunięta.")
                break
        else:
            print(f"Nie można usunąć. Notatka '{title}' nie istnieje.")


    def load_notes_from_hard_disc(self):
        pass

    def save_notes_to_hard_disc(self):
        pass
