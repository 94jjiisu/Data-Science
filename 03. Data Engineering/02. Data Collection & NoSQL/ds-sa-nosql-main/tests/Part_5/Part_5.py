import os
import csv

def test_collection(collection):
    def doc_counter(filt={}):
        return collection.count_documents(filt)

    test_filepath = os.path.join(os.getcwd(), 'titanic.csv')

    with open(test_filepath, 'r') as csvfile:
        test_data = [ d for d in csv.DictReader(csvfile)]

    survived_count = [d for d in test_data if d['Survived'] == '1']

    assert doc_counter() == len(test_data)
    assert doc_counter({'Survived': 1}) == len(survived_count)

def test_data_format(collection):
    sample_data = {
        'Survived' : 1,
        'Pclass': 3,
        'Name' : 'Miss. Laina Heikkinen',
        'Sex': 'female',
        'Age': 26.0,
        'Siblings/Spouses Aboard' : 0,
        'Parents/Children Aboard' : 0,
        'Fare': 7.925
    }

    coll_data = collection.find_one({'Name': 'Miss. Laina Heikkinen'})
    del coll_data['_id']

    assert coll_data == sample_data
    assert type(coll_data['Survived']) == int
    assert type(coll_data['Pclass']) == int
    assert type(coll_data['Name']) == str
    assert type(coll_data['Sex']) == str
    assert type(coll_data['Age']) == float
    assert type(coll_data['Siblings/Spouses Aboard']) == int
    assert type(coll_data['Parents/Children Aboard']) == int
    assert type(coll_data['Fare']) == float

