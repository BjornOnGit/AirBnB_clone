"""
creates a unique FileStorage instance for your application
"""
from .engine.file_storage import FileStorage
storage = FileStorage('models/engine/file.json')
storage.reload()
