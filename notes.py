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

    def refresh_titles_list(self):
        self.notes_titles_list = []
        for note in self.notes:
            self.notes_titles_list.append(note.title)

    def print_titles_list(self):
        self.refresh_titles_list()
        str_titles_list = ""
        if not self.notes_titles_list:
            return f"Lista notatek jest pusta, nie można wyświetlić tytułów"
        for title in self.notes_titles_list:
            str_titles_list += str(title) + "\n"
        return str_titles_list

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
