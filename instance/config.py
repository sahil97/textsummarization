import logging
import os

DEBUG=os.getenv("ENVIRONMENT") == "DEV"
HOST=os.getenv("APPLICATION_HOST")
PORT=int(os.getenv("APPLICATION_PORT", 3000))
