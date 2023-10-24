from pymongo.errors import ServerSelectionTimeoutError

from ui3.ui3 import Ui


def main():
    ui = Ui()
    try:
        print(f"Cześć! Próbuję nawiązać połączenie z Twoją bazą danych :)")
        ui.load_from_db()
    except ServerSelectionTimeoutError:
        print(f"Nie udało się nawiązać połączenia, sprawdź poprawność instalacji serwera MongoDb")
        return
    ui.run()


if __name__ == "__main__":
    main()
