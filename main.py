from wackywatch import *
def main():
    application = QApplication([])
    window = WackyWatch()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()