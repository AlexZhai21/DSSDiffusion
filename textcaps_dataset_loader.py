from datasets import load_dataset
from torch.utils.data import Dataset
import random

class TextCapsDataset(Dataset):
    def __init__(self, split="train"):
        self.data = load_dataset("lmms-lab/TextCaps", split=split)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        image = item["image"]
        captions = item.get("reference_strs", [])

        # pick one caption for training
        caption = random.choice(captions) if isinstance(captions, list) else captions

        ocr_tokens = item.get("ocr", [])

        return {
            "image": image,
            "caption": caption,
            "ocr_tokens": ocr_tokens
        }


if __name__ == "__main__":
    dataset = TextCapsDataset(split="train")
    sample = dataset[0]

    print("Caption:", sample["caption"])
    print("OCR tokens:", sample["ocr_tokens"])
    sample["image"].show()