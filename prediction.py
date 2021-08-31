from flash.text import TranslationTask

# 1. Load finetuned task
model = TranslationTask.load_from_checkpoint("https://flash-weights.s3.amazonaws.com/translation_model_en_ro.pt")

# 2. Translate a few sentences!
predictions = model.predict(
    [
        "BBC News went to meet one of the project's first graduates.",
        "A recession has come as quickly as 11 months after the first rate hike and as long as 86 months.",
    ]
)
print(predictions)