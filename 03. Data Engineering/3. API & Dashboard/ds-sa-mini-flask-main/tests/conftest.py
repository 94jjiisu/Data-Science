import os
import csv
import pytest
import sqlite3
import tempfile

from flask import Response
from mini_flask_app import create_app, CSV_FILEPATH

TEST_CSV_PATH = os.path.join(os.path.dirname(__file__), 'test.csv')

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def create_conn():
    conn = sqlite3.connect(TEST_DB_PATH)
    yield conn
    conn.close()
                
@pytest.fixture
def csv_operator():
    os.rename(CSV_FILEPATH, TEST_CSV_PATH)

    # initiate clean csv_file
    with open(CSV_FILEPATH, 'w') as inFile:
        fieldnames = ['id', 'username']
        csv_writer = csv.DictWriter(inFile, fieldnames=fieldnames)
        csv_writer.writeheader()

    operator = CSVOperator(CSV_FILEPATH)

    def returner():
        return operator

    yield returner

    os.rename(TEST_CSV_PATH, CSV_FILEPATH)


    
class CSVOperator:
    def __init__(self, csv_filepath=CSV_FILEPATH):
        self.filepath = csv_filepath
        self._fieldnames = ['id', 'username']

    def get_content(self):
        with open(self.filepath, 'r') as inFile:
            csv_reader = csv.DictReader(inFile)
            content = [_ for _ in csv_reader]

        return content


    def get_row(self, field, value):
        content = self.get_content()

        for row in content:
            if row.get(field, None) == value:
                return row


    def add_row(self, new_row):
        content = self.get_content()

        with open(self.filepath, 'w') as outFile:
            csv_writer = csv.DictWriter(outFile, fieldnames=self._fieldnames)

            csv_writer.writeheader()
            
            last_index = 0
            does_exist = False
            for row in content:
                if row['username'] == new_row['username']:
                    does_exist = True
                csv_writer.writerow(row)
                last_index = row['id']

            if not does_exist:
                new_row['id'] = int(last_index) + 1
                csv_writer.writerow(new_row)


    def update_row(self, prev_row, new_row):
        content = self.get_content()

        with open(self.filepath, 'w') as outFile:
            csv_writer = csv.DictWriter(outFile, fieldnames=self._fieldnames)

            csv_writer.writeheader()

            for row in content:
                if row == prev_row:
                    row = new_row

                csv_writer.writerow(row)

    def delete_row(self, field, value):
        content = self.get_content()

        with open(self.filepath, 'w') as outFile:
            csv_writer = csv.DictWriter(outFile, fieldnames=self._fieldnames)

            csv_writer.writeheader()

            for row in content:
                if row.get(field, None) != value:
                    csv_writer.writerow(row)
