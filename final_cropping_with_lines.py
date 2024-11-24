import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys


def process_image_and_detect_lines(image_path, debug_output_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 10)

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))

    horizontal_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    vertical_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=2)

    horizontal_contours, _ = cv2.findContours(horizontal_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    vertical_contours, _ = cv2.findContours(vertical_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    horizontal_positions = []
    for c in horizontal_contours:
        _, y, w, h = cv2.boundingRect(c)
        if w > 50:
            horizontal_positions.append(y)

    horizontal_positions = sorted(set(horizontal_positions))
    merged_horizontal_positions = []
    for i in range(len(horizontal_positions)):
        if i == 0 or horizontal_positions[i] - merged_horizontal_positions[-1] > 10:
            merged_horizontal_positions.append(horizontal_positions[i])

    vertical_positions = []
    for c in vertical_contours:
        x, _, w, h = cv2.boundingRect(c)
        if h > 50:
            vertical_positions.append(x)

    vertical_positions = sorted(set(vertical_positions))
    merged_vertical_positions = []
    for i in range(len(vertical_positions)):
        if i == 0 or vertical_positions[i] - merged_vertical_positions[-1] > 10:
            merged_vertical_positions.append(vertical_positions[i])

    debug_img = img.copy()

    for y in merged_horizontal_positions:
        cv2.line(debug_img, (0, y), (img.shape[1], y), (0, 255, 0), 2)

    for x in merged_vertical_positions:
        cv2.line(debug_img, (x, 0), (x, img.shape[0]), (255, 0, 0), 2)

    cv2.imwrite(debug_output_path, debug_img)

    return merged_horizontal_positions, merged_vertical_positions, debug_output_path


def crop_table_section(image_path, output_path, left_column_index=1, right_column_index=2):
    debug_output_path = "debug_lines.png"
    horizontal_positions, vertical_positions, debug_img = process_image_and_detect_lines(image_path, debug_output_path)

    if len(horizontal_positions) >= 3:
        top_y = horizontal_positions[2]
        bottom_y = max(horizontal_positions) if horizontal_positions else img.shape[0]
    else:
        raise ValueError("Not enough horizontal lines detected to crop from the third line onward.")

    if len(vertical_positions) > max(left_column_index, right_column_index):
        left_x = vertical_positions[left_column_index]
        right_x = vertical_positions[right_column_index]
    else:
        raise ValueError(
            f"Not enough vertical lines detected to use indices {left_column_index} and {right_column_index}."
        )

    top_left = (left_x, top_y)
    top_right = (right_x, top_y)
    bottom_left = (left_x, bottom_y)
    bottom_right = (right_x, bottom_y)

    img = cv2.imread(debug_img)
    cropped_img = img[top_y:bottom_y, left_x:right_x]

    cv2.imwrite(output_path, cropped_img)

    return top_left, top_right, bottom_left, bottom_right


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    image_path = sys.argv[1]

    debug_output_path = "debug_lines.png"
    output_path1 = "cropped_with_signature.png"
    output_path2 = "cropped_without_signature.png"

    coordinates_without_signature = crop_table_section(
        image_path, output_path2, left_column_index=1, right_column_index=2
    )
    coordinates_with_signature = crop_table_section(
        image_path, output_path1, left_column_index=1, right_column_index=3
    )
