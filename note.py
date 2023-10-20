from datetime import datetime


class Note:
    def __init__(self, title, note, creation_date=None, tag=None):
        self.title = title
        self.note = note
        if creation_date is None:
            self.creation_date = datetime.now()
        self.tag = tag

    def edit_note(self, title, new_note):
        self.title = title
        self.note = new_note
