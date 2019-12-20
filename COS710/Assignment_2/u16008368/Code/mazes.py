class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [
                {
                    'node': None,
                    'pheromone': 1,
                    'distance': None
                },
                {
                    'node': None,
                    'pheromone': 1,
                    'distance': None
                },
                {
                    'node': None,
                    'pheromone': 1,
                    'distance': None
                },
                {
                    'node': None,
                    'pheromone': 1,
                    'distance': None
                }
            ]
            self.pheromone = 1

    def __init__(self, im):

        width = im.size[0]
        height = im.size[1]
        data = list(im.getdata(0))

        self.start = None
        self.end = None

        # Top row buffer
        topnodes = [None] * width
        count = 0

        # Start row
        for x in range(1, width - 1):
            if data[x] > 0:
                self.start = Maze.Node((0, x))
                topnodes[x] = self.start
                count += 1
                break

        for y in range(1, height - 1):
            rowoffset = y * width
            rowaboveoffset = rowoffset - width
            rowbelowoffset = rowoffset + width

            # Initialise previous, current and next values
            prv = False
            cur = False
            nxt = data[rowoffset + 1] > 0

            leftnode = None

            for x in range(1, width - 1):
                # Move prev, current and next onwards. This way we read from the image once per pixel, marginal optimisation
                prv = cur
                cur = nxt
                nxt = data[rowoffset + x + 1] > 0

                n = None

                if not cur:
                    # ON WALL - No action
                    continue

                if prv:
                    if nxt:
                        # PATH PATH PATH
                        # Create node only if paths above or below
                        if data[rowaboveoffset + x] > 0 or data[rowbelowoffset + x] > 0:
                            n = Maze.Node((y, x))
                            distance = abs(n.Position[1] - leftnode.Position[1])
                            leftnode.Neighbours[1]['node'] = n
                            n.Neighbours[3]['node'] = leftnode
                            leftnode.Neighbours[1]['distance'] = distance
                            n.Neighbours[3]['distance'] = distance
                            leftnode = n
                    else:
                        # PATH PATH WALL
                        # Create path at end of corridor
                        n = Maze.Node((y, x))
                        distance = abs(n.Position[1] - leftnode.Position[1])
                        leftnode.Neighbours[1]['node'] = n
                        n.Neighbours[3]['node'] = leftnode
                        leftnode.Neighbours[1]['distance'] = distance
                        n.Neighbours[3]['distance'] = distance
                        leftnode = None
                else:
                    if nxt:
                        # WALL PATH PATH
                        # Create path at start of corridor
                        n = Maze.Node((y, x))
                        leftnode = n
                    else:
                        # WALL PATH WALL
                        # Create node only if in dead end
                        if (data[rowaboveoffset + x] == 0) or (data[rowbelowoffset + x] == 0):
                            # print ("Create Node in dead end")
                            n = Maze.Node((y, x))

                # If node isn't none, we can assume we can connect N-S somewhere
                if n is not None:
                    # Clear above, connect to waiting top node
                    if (data[rowaboveoffset + x] > 0):
                        t = topnodes[x]
                        distance = abs(n.Position[0] - t.Position[0])
                        t.Neighbours[2]['node'] = n
                        n.Neighbours[0]['node'] = t
                        t.Neighbours[2]['distance'] = distance
                        n.Neighbours[0]['distance'] = distance

                    # If clear below, put this new node in the top row for the next connection
                    if (data[rowbelowoffset + x] > 0):
                        topnodes[x] = n
                    else:
                        topnodes[x] = None

                    count += 1

        # End row
        rowoffset = (height - 1) * width
        for x in range(1, width - 1):
            if data[rowoffset + x] > 0:
                self.end = Maze.Node((height - 1, x))
                t = topnodes[x]
                distance = abs(t.Position[0] - self.end.Position[0])

                t.Neighbours[2]['node'] = self.end
                self.end.Neighbours[0]['node'] = t
                t.Neighbours[2]['distance'] = distance
                self.end.Neighbours[0]['distance'] = distance
                count += 1
                break

        self.count = count
        self.width = width
        self.height = height
