import cv2
import pandas as pd
import os


def annotate_image(image_path, ocr_results_path, output_path, font_scale=0.9, font_thickness=2):
    img = cv2.imread(image_path)

    ocr_data = pd.read_csv(ocr_results_path)

    for _, row in ocr_data.iterrows():
        text = row["text"]
        y = int(row["y"])

        x = 10
        position = (x, y)

        cv2.putText(
            img,
            text,
            position,
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            (0, 0, 255),
            font_thickness,
            lineType=cv2.LINE_AA,
        )

    cv2.imwrite(output_path, img)


if __name__ == "__main__":
    IMAGE_PATH = "cropped_without_signature.png"
    OCR_RESULTS_PATH = "ocr_results.csv"
    OUTPUT_PATH = "annotated_image.png"

    annotate_image(IMAGE_PATH, OCR_RESULTS_PATH, OUTPUT_PATH)
