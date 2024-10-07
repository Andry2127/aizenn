import logging
import sys

from app import app

if __name__ == "__name__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    app.run(debug=True)



