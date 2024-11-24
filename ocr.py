from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
import torch
import pandas as pd


def filter_and_merge_texts(jsonka, confidence_threshold=0.50, vertical_tolerance=5, horizontal_tolerance=50):
    filtered_data = [entry for entry in jsonka[0].text_lines if entry.confidence > confidence_threshold]

    df = pd.DataFrame([{"x": entry.bbox[0], "y": entry.bbox[3], "text": entry.text} for entry in filtered_data])
    df = df.sort_values(["y", "x"]).reset_index(drop=True)

    merged_data = []
    current_y = None
    current_texts = []
    current_x = None

    for _, row in df.iterrows():
        if current_y is None or (
            abs(row["y"] - current_y) <= vertical_tolerance
            and (current_x is None or abs(row["x"] - current_x) <= horizontal_tolerance)
        ):
            if current_y is None:
                current_y = row["y"]
            current_x = row["x"]
            current_texts.append(row["text"])
        else:
            merged_data.append({"y": current_y, "text": " ".join(current_texts)})
            current_y = row["y"]
            current_x = row["x"]
            current_texts = [row["text"]]

    if current_texts:
        merged_data.append({"y": current_y, "text": " ".join(current_texts)})

    result_df = pd.DataFrame(merged_data)
    return result_df


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

IMAGE_PATH = "cropped_without_signature.png"
image = Image.open(IMAGE_PATH)

langs = ["en"]

det_processor, det_model = load_det_processor(), load_det_model()
rec_model, rec_processor = load_rec_model(), load_rec_processor()

det_model = det_model.to(device)
rec_model = rec_model.to(device)


def run_ocr_with_device(images, langs, det_model, det_processor, rec_model, rec_processor):
    det_model.eval()
    rec_model.eval()

    predictions = run_ocr(images, langs, det_model, det_processor, rec_model, rec_processor)
    return predictions


predictions = run_ocr_with_device([image], [langs], det_model, det_processor, rec_model, rec_processor)

df_result = filter_and_merge_texts(
    predictions, confidence_threshold=0.50, vertical_tolerance=10, horizontal_tolerance=200
)

df_result.to_csv("ocr_results.csv", index=False)
