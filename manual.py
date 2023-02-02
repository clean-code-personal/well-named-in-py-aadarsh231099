from color_pair import *
def print_color_coding_reference():
    print("Color Coding Reference:")
    for major_index, major_color in enumerate(MAJOR_COLORS):
        for minor_index, minor_color in enumerate(MINOR_COLORS):
            pair_number = major_index * len(MINOR_COLORS) + minor_index + 1
            color_pair = color_pair_to_string(major_color, minor_color)
            print(f"{pair_number}. {color_pair}")