from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_knowledge():
    with open("knowledge.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def chat_response(user_input):
    data = load_knowledge()
    data_embeddings = model.encode(data, convert_to_tensor=True)
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(input_embedding, data_embeddings)
    best_index = torch.argmax(scores)
    best_score = scores[0][best_index].item()

    if best_score > 0.5:
        return data[best_index]
    else:
        return "Bro, mujhe iska jawaab nahi mil raha. Thoda aur data de mujhe seekhne ke liye!"
