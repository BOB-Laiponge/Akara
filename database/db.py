import sys

import psycopg2


async def execute_sql(operations, fetch, client=None, error_channel=None):
    """
        Executes a request (or many requests in the database)
        Operations are all the queries, given in SQL language.
        The fetch operation is executed at the end of all the operations
        fetch (int from 0 to whatever) :
            -1 will call fetchall
            1 will call fetchone
            Any other positive number will call fetchmany
            Any other negative number will disable fetch operation
    """
    db = psycopg2.connect(sys.argv[2], sslmode='require')
    db_cursor = db.cursor()
    res = None
    for operation in operations:
        try:
            db_cursor.execute(operation)
        except Exception as e:
            if client is not None:
                if error_channel is None:
                    error_channel = client.get_channel(420320011668946944)
                await error_channel.send("Désolée, il y a eu une erreur lors de la communication avec la base "
                                         "de données: " + str(e))
    try:
        if fetch == -1:
            res = db_cursor.fetchall()
        elif fetch == 1:
            res = db_cursor.fetchone()
        elif fetch == 1.0:
            res = db_cursor.fetchmany(1)
        elif fetch > 1:
            res = db_cursor.fetchmany(fetch)
        elif fetch == 0:
            raise ValueError("Cannot fetch negative number of values")
    except Exception as e:
        if client is not None:
            if error_channel is None:
                error_channel = client.get_channel(420320011668946944)
            await error_channel.send("Désolée, il y a eu une erreur lors de la communication avec la base "
                                     "de données: " + str(e))
    finally:
        db_cursor.close()
        db.commit()
        db.close()
    return res


def db_escape_string(s):
    return s.replace("'", "''")
