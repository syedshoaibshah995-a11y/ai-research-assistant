from transformers import pipeline

paraphraser = pipeline("text2text-generation", model="t5-base")

def paraphrase_text(text):
    try:
        if len(text) > 512:
            text = text[:512]

        prompt = "paraphrase: " + text
        result = paraphraser(prompt, max_length=200)

        return result[0]['generated_text']

    except Exception as e:
        return f"Error in paraphrasing: {e}"
