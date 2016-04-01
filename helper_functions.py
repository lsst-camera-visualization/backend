import six
import os

def valid_boundary(boundary):
    try:
        boundary = list(map(int, boundary))
    except:
        boundary = [0, 1, 0, 1]
    x_start, x_end = boundary[0], boundary[2]
    y_start, y_end = boundary[1], boundary[3]
    # os.system("echo %d %d %d %d > /www/algorithm/debug_file" % (x_start, x_end, y_start, y_end))
    if (x_start > x_end):
        x_start, x_end = x_end, x_start
    if (y_start > y_end):
        y_start, y_end = y_end, y_start
    return x_start, x_end, y_start, y_end

def rect2slice(region):
    if (region.get('rect')):
        shape = region['rect']
        return (slice(shape['top'],shape['bottom']), slice(shape['left'],shape['right']))
    else:
        return (slice(),slice())

# TODO: define a function that checks valid filenames
def valid_filename(filename):
    return filename
