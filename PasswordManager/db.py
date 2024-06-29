import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                platform TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        self.close()

    def add_new_data(self, platform, password):
        try:
            self.connect()
            self.cursor.execute('''
                INSERT INTO passwords (platform, password)
                VALUES (?, ?)
            ''', (platform, password))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError(f"{platform} already exists.")

        finally:
            self.close()

    def update_data(self, platform, password):
        try:
            self.connect()
            self.cursor.execute('''
                UPDATE passwords
                SET password = ?
                WHERE platform = ?
            ''', (password, platform))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                return False 
            else:
                return True  

        finally:
            self.close()

    def delete_data(self, platform):
        try:
            self.connect()
            self.cursor.execute('''
                DELETE FROM passwords
                WHERE platform = ?
            ''', (platform,))
            self.conn.commit()
            if(self.cursor.rowcount == 0):
                return False
            else:
                return True
        finally:
            self.close()

    def get_password_list(self):
        try:
            self.connect()
            self.cursor.execute('SELECT * FROM passwords')
            return self.cursor.fetchall()
        finally:
            self.close()

    def get_platform_list(self):
        try:
            self.connect()
            self.cursor.execute('SELECT platform FROM passwords')
            return self.cursor.fetchall()
        finally:
            self.close()


    def get_password_for_one_platform(self,platform):
        try:
            self.connect()
            self.cursor.execute('SELECT * FROM passwords WHERE platform=?',(platform,))
            return self.cursor.fetchone()
        finally:
            self.close()
    def delete_all_datas(self):
        try:
            self.connect()
            self.cursor.execute("DELETE FROM passwords")
            self.conn.commit()
        finally:
            self.close()
