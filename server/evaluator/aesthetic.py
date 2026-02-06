import torch
from PIL import Image
import io

from aesthetic_predictor_v2_5 import convert_v2_5_from_siglip


class AestheticScorer:
    def __init__(self, device: str | None = None):
        self.device = device or (
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        # load model + preprocessor فقط یک‌بار
        self.model, self.preprocessor = convert_v2_5_from_siglip(
            low_cpu_mem_usage=True,
            trust_remote_code=True
        )

        self.model = self.model.to(self.device)
        self.model.eval()

    def score(self, image_bytes: bytes) -> float:
        """
        image_bytes: raw bytes of image (e.g. from Figma export)
        """
        # 1. bytes → PIL Image
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # 2. preprocess → tensor
        inputs = self.preprocessor(
            images=img,
            return_tensors="pt"
        ).pixel_values.to(self.device)

        # 3. inference
        with torch.inference_mode():
            score = (
                self.model(inputs)
                .logits
                .squeeze()
                .float()
                .cpu()
                .item()
            )

        return score
