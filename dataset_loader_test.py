from textcaps_dataset_loader import TextCapsDataset

dataset = TextCapsDataset(split="train")
sample = dataset[0]

print(sample["caption"])
print(sample["ocr_tokens"])