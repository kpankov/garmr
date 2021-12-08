import sqlite3
from os import curdir
from os import path


class Database:
    database_file_path = path.join(curdir, "garmr.sqlite")
    schema_file_path = path.join(curdir, "schema.sql")

    def __init__(self):
        pass

    def init_db(self):
        connection = sqlite3.connect(self.database_file_path)

        with open(self.schema_file_path) as f:
            connection.executescript(f.read())

        cur = connection.cursor()

        cur.execute("INSERT INTO ips (name) VALUES (?)", ("None",))

        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_0', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_1', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_2', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_3', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_4', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_5', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_6', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_7', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_8', 1))
        cur.execute("INSERT INTO testbeds (name, ip_id) VALUES (?, ?)", ('FPGA_9', 1))

        connection.commit()
        connection.close()

        print("OK")

    def __get_db_connection(self):
        conn = sqlite3.connect(self.database_file_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _fetch_all(self, *sql):
        conn = self.__get_db_connection()
        rows = conn.execute(*sql).fetchall()
        conn.close()
        return rows

    def get_list(self):
        rows = self._fetch_all("SELECT testbeds.name, ips.ip FROM testbeds, ips WHERE testbeds.ip_id == ips.id")
        if not bool(rows):
            return None
        testbeds = []
        for row in rows:
            testbeds.append({"name": row["name"], "address": row["ip"]})

        return testbeds

    def get_ips(self):
        print(self._fetch_all("SELECT * FROM ips"))
