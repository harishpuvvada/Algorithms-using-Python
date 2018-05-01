'''
Given two rectangles, determine if they overlap.

 The rectangles are defined as a Dictionary

r1 = {
         # x and y coordinates of the bottom-left corner of the rectangle
         'x': 2 , 'y': 4,

         # Width and Height of rectangle
         'w':5,'h':12

         }
'''



def calc_overlap(coor1,dim1,coor2,dim2):
    """
    Takes in 2 coordinates and their length in that dimension
    """

    # Find greater of the two coordinates
    # (this is either the point to the most right
    #  or the higher point, depending on the dimension)

    # The greater point would be the start of the overlap
    greater = max(coor1,coor2)

    # The lower point is the end of the overlap
    lower = min(coor1+dim1,coor2+dim2)

    # Return a tuple of Nones if there is no overlap

    if greater >= lower:
        return (None,None)

    # Otherwise, get the overlap length
    overlap = lower-greater

    return (greater,overlap)


def calc_rect_overlap(r1,r2):


    x_overlap, w_overlap = calc_overlap(r1['x'],r1['w'],r2['x'],r2['w'])

    y_overlap, h_overlap = calc_overlap(r1['y'],r1['h'],r2['y'],r2['h'])

    # If either returned None tuples, then there is no overlap!
    if not w_overlap or not h_overlap:
        print 'There was no overlap!'
        return None

    # Otherwise return the dictionary format of the overlapping rectangle
    return { 'x':x_overlap,'y': y_overlap,'w':w_overlap,'h':h_overlap}



r1 = {'x': 2 , 'y': 4,'w':5,'h':12}
r2 = {'x': 1 , 'y': 5,'w':7,'h':14}
calc_rect_overlap(r1,r2)

#{'h': 11, 'w': 5, 'x': 2, 'y': 5}
