import pytest


@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import linked_list
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


@pytest.mark.timeout(10)
def test_part2_working_normally():
    from src.Part_2 import linked_list
    from random import shuffle

    try:
        test_li = ([n for n in range(0,10)])
        shuffle(test_li)

        ll = linked_list(test_li[0])

        for idx in range(1, len(test_li)):
            ll.add_node(test_li[idx])

        for num in range(0,len(test_li)):
            assert num == ll.search_node(num).value, \
                'search_node는 연결리스트의 찾고자 하는 value값을 가진 노드를 반환해야합니다.'

        assert None == ll.search_node(100), \
            'linkedlist에 찾고자 하는 값이 없는 경우 search_node는 -1을 반환해야합니다.'
        
        for i in range(0,len(test_li)):
            test_li.remove(i)
            assert i == ll.del_node(i), \
                'del_node가 정상적으로 작동해야합니다. 삭제를 진행한 경우 삭제한 value값을 반환해야합니다.'
            assert test_li == ll.ord_desc(), \
                '연결리스트에 남아있는 값을 리스트 형태로 반환해주세요.'


    except Exception as e:
        pytest.fail(f'{e} \n 에러가 발생하였습니다. 코드를 다시 한 번 확인해주세요.')
        