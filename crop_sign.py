import os
import pandas as pd
import cv2


def crop_signatures_with_expanded_range(
    cropped_image_path, ocr_results_path, output_directory, y_adjustment=0, range_expansion=5
):
    ocr_data = pd.read_csv(ocr_results_path)

    ocr_data["y"] = ocr_data["y"] + y_adjustment

    os.makedirs(output_directory, exist_ok=True)

    cropped_img = cv2.imread(cropped_image_path)
    if cropped_img is None:
        raise FileNotFoundError(f"Image not found at path: {cropped_image_path}")

    ocr_data = ocr_data.sort_values(by="y")
    y_coords = [0] + ocr_data["y"].tolist()
    names = ocr_data["text"].tolist()

    for i in range(len(y_coords) - 1):
        y_start = int(y_coords[i]) - range_expansion
        y_end = int(y_coords[i + 1]) + range_expansion

        y_start = max(0, y_start)
        y_end = min(cropped_img.shape[0], y_end)

        cropped_signature = cropped_img[y_start:y_end, :]

        output_path = os.path.join(output_directory, f"{names[i]}.png")
        cv2.imwrite(output_path, cropped_signature)


cropped_image_path = "cropped_output1.png"
ocr_results_path = "ocr_results.csv"
output_directory = "signatures"
y_adjustment = 7
range_expansion = 3

crop_signatures_with_expanded_range(
    cropped_image_path, ocr_results_path, output_directory, y_adjustment, range_expansion
)
