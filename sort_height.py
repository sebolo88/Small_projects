#!/usr/bin/env python3

def value_getter(item):
    return item[1]


def sort_height(names, heights):
    height_dict = {}
    height_order = []
    for index, name in enumerate(names):
        height_dict[name] = heights[index]
    # print(height_dict)
    for name, height in sorted(height_dict.items(), key=value_getter, reverse=True):
        height_order.append(name)
    # print(height_order)
    return height_order


print(sort_height(["Mary", "John", "Emma"], [180, 165, 170]))
