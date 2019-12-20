from PIL import Image
import time
from mazes import Maze
import beam_search
from aco import ACO

Image.MAX_IMAGE_PIXELS = 10000000000

def solve(input_file, output_file):
    print("Create Maze")
    im = Image.open(input_file)
    start_time = time.time()
    maze = Maze(im)
    print("Node Count:", maze.count)
    print("Time elapsed:", time.time() - start_time, "\n")

    print("Solving")
    start_time = time.time()
    # [result, stats] = beam_search.solve(maze.start, maze.end, maze.width, maze.width)
    aco = ACO(maze_width=maze.width, num_ants=3, start_node=maze.start, end_node=maze.end, alpha=1,
              beta=3, global_evaporation_rate=0.6, local_evaporation_rate=0.1, r_constant=0.9, q_constant=2)
    [result, stats] = aco.solve(epoch=3)
    print("Time elapsed: ", time.time() - start_time, "\n")
    print("Longest Distance: ", stats[0], "\n")

    print_image(im, result, output_file)


def print_image(im, resultpath, output_file):
    print("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()
    # comment this out when using ant
    # resultpath = [node.Position for node in resultpath]
    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i + 1]

        px = (255, 0, 0)

        if a[0] == b[0]:
            for x in range(min(a[1], b[1]), max(a[1], b[1])):
                impixels[x, a[0]] = px
        elif a[1] == b[1]:
            for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                impixels[a[1], y] = px

    im.save(output_file)

# print("===== SMALL 1 ==========")
# solve("./Mazes/Small1.bmp", "./Output2/Small1.png")
# print("===== SMALL 2 ==========")
# solve("./Mazes/Small2.bmp", "./Output2/Small2.png")
# print("===== Small-Medium 1 ==========")
# solve("./Mazes/Small-Medium1.bmp", "./Output2/Small-Medium1.png")
# print("===== Small-Medium 2 ==========")
# solve("./Mazes/Small-Medium2.bmp", "./Output2/Small-Medium2.png")
# print("===== Small-Medium 3 ==========")
# solve("./Mazes/Small-Medium3.bmp", "./Output2/Small-Medium3.png")
# print("===== Medium 1 ==========")
# solve("./Mazes/Medium1.bmp", "./Output2/Medium1.png")
# print("===== Medium 2 ==========")
# solve("./Mazes/Medium2.bmp", "./Output2/Medium2.png")
# print("===== Medium 3 ==========")
# solve("./Mazes/Medium3.bmp", "./Output2/Medium3.png")
# print("===== Large 1 ==========")
# solve("./Mazes/Large1.bmp", "./Output2/Large1.png")

# print("===== SMALL 1 ==========")
# solve("./Mazes/Small1.bmp", "./Output/Small1.png")
# print("===== SMALL 2 ==========")
# solve("./Mazes/Small2.bmp", "./Output/Small2.png")
# print("===== Small-Medium 1 ==========")
# solve("./Mazes/Small-Medium1.bmp", "./Output/Small-Medium1.png")
# print("===== Small-Medium 2 ==========")
# solve("./Mazes/Small-Medium2.bmp", "./Output/Small-Medium2.png")
# print("===== Small-Medium 3 ==========")
# solve("./Mazes/Small-Medium3.bmp", "./Output/Small-Medium3.png")
# print("===== Medium 1 ==========")
# solve("./Mazes/Medium1.bmp", "./Output/Medium1.png")
# print("===== Medium 2 ==========")
# solve("./Mazes/Medium2.bmp", "./Output/Medium2.png")
# print("===== Medium 3 ==========")
# solve("./Mazes/Medium3.bmp", "./Output/Medium3.png")
print("===== Large 1 ==========")
# solve("./Mazes/Large1.bmp", "./Output/Large1.png")

solve("./Mazes/Large1.bmp", "output.png")
