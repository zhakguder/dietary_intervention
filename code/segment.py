#!/usr/bin/env python3

from food_segmentation import initial_boxes

initial_boxes.IMG_PATH = '~/Desktop/apples.jpeg'

initial_boxes.watershed()
# initial_boxes.get_boxes()
# grouped = initial_boxes.group_boxes()
# initial_boxes.visualize(grouped)
# breakpoint()
