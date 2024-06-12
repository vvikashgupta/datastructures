#!/usr/local/bin/python
# sqrt of points ...lowest one is closer to origin
def close_point(points , k):
    points.sort(key=lambda x: x[0]** 2 + x[1]**2)
    return points[:k]
