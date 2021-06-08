from fileShareApp import create_app
from logging import FileHandler, DEBUG

file_handler = FileHandler('run_error_log.txt')
file_handler.setLevel(DEBUG)


app = create_app()

app.logger.addHandler(file_handler)


if __name__ == "__main__":
    app.run()
