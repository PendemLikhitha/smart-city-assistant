# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

model_name = "ibm-granite/granite-3.3-2b-instruct"

# Load model and tokenizer (put inside try-except to catch errors early)
try:
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except Exception as e:
    print("Error loading model:", e)
    raise e

class QueryRequest(BaseModel):
    query: str
def generate_response(query):
    chat = [{"role": "user", "content": query}]
    
    input_ids = tokenizer.apply_chat_template(
        chat, return_tensors="pt", add_generation_prompt=True
    ).to(model.device)

    # Manually create attention mask
    attention_mask = (input_ids != tokenizer.pad_token_id).long()

    with torch.no_grad():
        output_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )

    response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)
    return response.strip()



@app.get("/")
def read_root():
    return {"message": "Smart City Assistant Backend is running 🚀"}

@app.post("/chat/")
async def chat(request: QueryRequest):
    try:
        reply = generate_response(request.query)
        return {"response": reply}
    except Exception as e:
        return {"response": f"❌ Error during generation: {e}"}