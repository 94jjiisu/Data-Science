
from src import Part1
from tests import Hash



def test_part1_1():
    assert Hash.md5_hash(Part1.n312_part1_1()) == '5357da4895393188c7991d6b93711b71'

def test_part1_2():
    assert Hash.md5_hash(Part1.n312_part1_2()) == 'a537e89aa6c23c74625b92b7711b6a14'

def test_part1_3():
    assert Hash.getHash(Part1.n312_part1_3()) == 'ac64c3315bb965b921351887647aab47'