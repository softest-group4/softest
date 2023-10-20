class Notes:
    BACKUP_FILENAME = "notes_backup.txt"

    def __init__(self, notes):
        self.notes = notes
        self.notes_titles_list = None

    def add_new_note(self, new_note):
        self.notes.append(new_note)

    def check_if_note_exists_in_notes(self, title):
        for existing_note in self.notes:
            if existing_note.title == title:
                return f"{title} already exists in the base."
            return f"{title} does not exist in the base."

    def get_note_from_notes(self, title):
        for existing_note in self.notes:
            if existing_note.title == title:
                return existing_note
            return None

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

    def get_titles_list(self):
        self.notes_titles_list = []
        for note in self.notes:
            self.notes_titles_list.append(note.title)
        return self.notes_titles_list

    def get_content_from_note(self, note_title):
        title = note_title
        note = self.get_note_from_notes(title)
        if not note:
            return f"Niepowodzenie! Nie znaleziono notatki o podanym tytule"
        return f"Treść notatki: {note.note}"

    def load_notes_from_hard_disc(self):
        pass

    def save_notes_to_hard_disc(self):
        pass
