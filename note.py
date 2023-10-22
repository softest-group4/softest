from datetime import datetime


class Note:
    def __init__(self, title, note, creation_date=None, tag=None):
        self.title = title
        self.note = note
        if creation_date is None:
            self.creation_date = datetime.now()
        self.tag = tag

    def __str__(self):
        str_contact = f"{self.title}     "
        if len(self.note) > 0:
            str_contact += f"treść notatki: {self.note}   "
        str_contact += "\n"
        return str_contact

    def edit_note(self, title, new_note):
        self.title = title
        self.note = new_note
