import unittest

import yaml
import psycopg2

class TestDatatypes(unittest.TestCase):

    def setUp(self):
        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
            self.conn = psycopg2.connect(database=config['DATABASE']['DB'],
                                         user=config['DATABASE']['USERNAME'],
                                         password=config['DATABASE']['PASSWORD'],
                                         host=config['DATABASE']['HOST'],
                                         port=config['DATABASE']['PORT'])
        except:
            print('Error')
        finally:
            pass

    def test_datatypes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT column_name, data_type FROM\
                        information_schema.columns WHERE table_name = 'prices'")
        res =  cursor.fetchall()
        #check the data types of open, high, low, close
        for row in res:
            if row[1] in ('open', 'high', 'low', 'close'):
                self.assertEqual(row[2], 'double precision')
            elif row[1] == 'volume':
                self.assertEqual(row[2], 'bigint')
            elif row[1] == 'instrument':
                self.assertEqual(row[2], 'text')
            elif row[1] == 'datetime':
                self.assertEqual(row[2], 'timestamp without time zone')

if __name__ == '__main__':
    unittest.main()
