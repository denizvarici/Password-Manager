import os

class FolderManager:
    def __init__(self,db_path):
        self.db_path = db_path

    def check_directory(self):
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
