from collections import deque


def solve(node_start, node_end, width, beam_width):
    node_start.Neighbours[0]['parent'] = None
    prio_queue = deque([(node_start, 10)])
    visited = [False] * (width ** 2)
    visited[node_start.Position[0] * width + node_start.Position[1]] = True

    while prio_queue:
        prio_queue = sorted(prio_queue, key=lambda tup: tup[1], reverse=True)
        prio_queue = prio_queue[:beam_width]
        current = prio_queue.pop()

        if current[0].Position == node_end.Position:
            break

        for index, n in enumerate(current[0].Neighbours):
            if n['node'] is not None:
                pos = n['node'].Position[0] * width + n['node'].Position[1]
                if not(visited[pos]):
                    prio = calc_heuristic(index, n['distance'])
                    prio_queue.append((n['node'], prio))
                    visited[pos] = True
                    n['node'].Neighbours[0]['parent'] = (current[0], n['distance'])

    path = deque()
    path.append(current[0])
    total_distance = 1
    current = current[0].Neighbours[0]['parent']
    while (current is not None):
        path.append(current[0])
        total_distance += current[1]
        current = current[0].Neighbours[0]['parent']

    return [path, [total_distance]]


def calc_heuristic(index, distance):
    if index == 0:
        return distance * 0.5
    if index == 2:
        return distance * 0.9
    else:
        return distance * 0.75
