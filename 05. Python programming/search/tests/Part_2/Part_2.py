import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import char_combi

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part2_char_combi():
    from src.Part_2 import char_combi

    assert char_combi('2') == ['q', 'w', 'e'], "매개변수로 '2'가 들어갔을 때 정확한 값을 반환해야합니다."
    assert char_combi('3') == ['a', 's', 'd'], "매개변수로 '3'이 들어갔을 때 정확한 값을 반환해야합니다."
    assert char_combi('4') == ['z', 'x', 'c'], "매개변수로 '4'가 들어갔을 때 정확한 값을 반환해야합니다."
    assert char_combi('23') == ['qa', 'qs', 'qd', 'wa', 'ws', 'wd', 'ea', 'es', 'ed'], "매개변수로 '23'이 들어갔을 때 정확한 값을 반환해야합니다."
    assert char_combi('34') == ['az', 'ax', 'ac', 'sz', 'sx', 'sc', 'dz', 'dx', 'dc'], "매개변수로 '34'가 들어갔을 때 정확한 값을 반환해야합니다."
    assert char_combi('24') == ['qz', 'qx', 'qc', 'wz', 'wx', 'wc', 'ez', 'ex', 'ec'], "매개변수로 '24'가 들어갔을 때 정확한 값을 반환해야합니다."
    assert char_combi('234') == ['qaz', 'qax', 'qac', 'qsz', 'qsx', 'qsc', 'qdz', 'qdx', 'qdc', 'waz', 'wax', 'wac', 'wsz', 'wsx', 'wsc', 'wdz', 'wdx', 'wdc', 'eaz', 'eax', 'eac', 'esz', 'esx', 'esc', 'edz', 'edx', 'edc'], "매개변수로 '234'가 들어갔을 때 정확한 값을 반환해야합니다."