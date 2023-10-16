from ui import Ui


def main():
    ui = Ui()
    ui.load_from_db()
    ui.run()


if __name__ == "__main__":
    main()
