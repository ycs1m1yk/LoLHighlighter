import numpy as np

total_time = 2963
hits_remove_dup = [7, 82, 109, 239, 240, 241, 255, 259, 336, 352, 402, 408, 410, 640, 715, 722, 723, 725, 730, 731,
                   735, 738, 739, 759, 778, 800, 1025, 1039, 1213, 1338, 1424, 1426, 1428, 1466, 1475, 1502, 1637, 1639, 1654, 1673, 1784, 1788, 1798, 1895, 1899, 1945, 2477, 2478, 2521, 2534, 2611, 2692, 2693, 2694, 2695, 2696, 2762, 2813, 2819, 2824, 2829, 2830, 2831, 2880, 2881, 2915, 2927, 2955, 2962, 2963]


hl_start = hits_remove_dup[0]
hl_temp = hits_remove_dup[0]
hl_end = hits_remove_dup[1]

hl_list = []
iteration = 1

print(hits_remove_dup[len(hits_remove_dup)-1])
# while iteration < len(hits_remove_dup):
#     count = 0
#     while hl_end - hl_temp < 10:

#         if iteration == len(hits_remove_dup):
#             break
#         hl_end = hits_remove_dup[iteration]
#         hl_temp = hits_remove_dup[iteration-1]
#         iteration += 1
#         count += 1

#     if hl_end != total_time:
#         if count > 1:
#             element = [hl_start, hl_temp]
#             hl_list.append(element)

#         hl_start = hits_remove_dup[iteration]
#         hl_temp = hits_remove_dup[iteration]
#         hl_end = hits_remove_dup[iteration+1]

#     iteration += 1

# print(hl_list)
