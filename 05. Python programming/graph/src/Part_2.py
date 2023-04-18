"""
Bare Minimum Requirements
    그래프에서 활용되는 기본 요소인 인접리스트를 다양하게 활용합니다.

요구사항:
    과거부터 지금까지 이슈화되고 많이 활용되는 최단경로에 대해 생각해봅니다.

    Part 1에서 구성된 인접리스트와 코드를 기반으로, 시작노드와 끝노드에 따라 최단경로를 찾도록 구성하세요.
    최단경로에 대해 해결했다면 가중치값을 활용한 경로의 다양성에 대해 구성해보도록 해봅시다.

    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        connection_info = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
        }
        search_shortest_route(connection_info, 'B', 'D')

    출력값:
        ['B', 'D']
"""


def search_shortest_route(connection_info, start_node, end_node, route=[]):
    route = route + [start_node]
    if start_node == end_node:
        return route

    if not connection_info.__contains__(start_node):
        return None

    shortest = None
    for node in connection_info[start_node]:
        if end_node in connection_info[start_node]:
            return route + [end_node]
        else:
            return search_shortest_route(connection_info, node, end_node, route=route)
