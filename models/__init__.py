#!/usr/bin/python3

"""
init package to create a unique FileStorage
instance for your application
"""

from .engine.file_storage import FileStorage

storage = FileStorage() # create the variable storage, an instance of FileStorage
storage.reload() # call reload() method on this variable
