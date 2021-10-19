import sqlite3


def connect_to_database(f):
    def wrap(self, *args):
        # self = args[0]
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        connected = f(self, cur, *args)
        return connected
    return wrap


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    @connect_to_database
    def __len__(self, cursor):
        cursor.execute(f'select count(*) from {self.table_name}')
        return cursor.fetchone()[0]

    @connect_to_database
    def __getitem__(self, cursor, item):
        cursor.execute(f'select * from {self.table_name} where name=:name',
                       {'name': item})
        return cursor.fetchall()

    @connect_to_database
    def __iter__(self, cursor):
        self.cursor = cursor
        self.cursor.execute(f'select * from {self.table_name}')
        self.columns = [x[0] for x in cursor.description]
        return self

    @connect_to_database
    def __next__(self, *args):
        row = self.cursor.fetchone()
        if row is None:
            raise StopIteration
        return dict(zip(self.columns, row))

    @connect_to_database
    def __contains__(self, cursor, item):
        cursor.execute(
            f'select * from {self.table_name} where name =:name',
            {'name': item}
        )
        return cursor.fetchone()
