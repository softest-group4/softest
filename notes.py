class Notes:
    BACKUP_FILENAME = "notes_backup.txt"

    def __init__(self, notes):
        self.notes = notes
        self.notes_titles_list = None

    def add_new_note(self, new_note):
        if self.check_if_note_exists_in_notes(new_note.title):
            return (f'Niepowodzenie! Notatka o tytule {new_note.title} już istnieje, wybierz inne tytuł notatki '
                    f'stosując indeksację, np {new_note.title}_1212')
        self.notes.append(new_note)
        return "Sukces!"

    def check_if_note_exists_in_notes(self, title):
        for existing_note in self.notes:
            if existing_note.title == title:
                return True
        return False

    def get_note_from_notes(self, title):
        for existing_note in self.notes:
            if existing_note.title == title:
                return existing_note
        return None

    def edit_note_in_notes(self, title, new_title, new_content):
        note_to_edit = self.get_note_from_notes(title)

        if note_to_edit:
            if new_title:
                note_to_edit.title = new_title
            if new_content:
                note_to_edit.content = new_content
                return f"Sukces!"
        else:
            return f"Nie znaleziono notatki '{title}'."

    def delete_note_from_notes(self, title):
        note_to_delete = self.get_note_from_notes(title)

        if note_to_delete:
            self.notes.remove(note_to_delete)
            return f"Sukces!"
        else:
            return f"Nie można usunąć. Notatka '{title}' nie istnieje."

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

    def get_whole_notes(self):
        str_notes = f"\nLista notatek jest następująca:\n"
        for note in self.notes:
            str_notes += str(note)
        str_notes += f"------------------------------------------------------------\n"
        return str_notes
