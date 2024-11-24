import numpy as np
import cv2


def detect_and_crop_from_right(image_path, annotated_output_path, cropped_output_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(gray_blurred, 50, 150, apertureSize=3)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 9))
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    image_height = img.shape[0]

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=int(0.5 * image_height), maxLineGap=10)

    vertical_lines = []
    rightmost_x = img.shape[1]
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                if abs(x2 - x1) < 10:
                    vertical_lines.append((x1, y1, x2, y2))
                    rightmost_x = min(rightmost_x, x1, x2)

    annotated_img = img.copy()
    for x1, y1, x2, y2 in vertical_lines:
        cv2.line(annotated_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(
        annotated_img, f"Vertical Lines: {len(vertical_lines)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
    )

    cv2.imwrite(annotated_output_path, annotated_img)

    if len(vertical_lines) == 0:
        raise ValueError("No vertical lines detected. Unable to crop the image.")

    cropped_img = img[:, rightmost_x:]

    if cropped_img.size == 0:
        raise ValueError(f"Cropping failed. Invalid dimensions: {cropped_img.shape}")

    cv2.imwrite(cropped_output_path, cropped_img)

    return len(vertical_lines), annotated_output_path, cropped_output_path


line_count, annotated_output_path, cropped_output_path = detect_and_crop_from_right(
    "cropped_with_signature.png", "annotated_output1.png", "cropped_output1.png"
)

line_count, annotated_output_path, cropped_output_path
