import os

HOST = os.getenv('HOST') or '127.0.0.1'
PORT = os.getenv('PORT') or '8050'
MULLER_MAP_BACKEND = os.getenv('MULLER_MAP_BACKEND') or 'http://127.0.0.1:8080/v2'
