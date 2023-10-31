from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import JSONResponse

from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

from pydantic import BaseModel

class InputList(BaseModel):
    inputList: list[str]

app = FastAPI()

# Define core policies and security headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You should specify the allowed origins in a production environment.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)


# Define a sample API endpoint
@app.post("/api/text-embeddings")
async def process_embeddings(inputList: InputList):
    
    path_to_model ='./Model'
    # Sentences we want sentence embeddings for
    sentences = inputList.inputList #['This is an example sentence', 'Each sentence is converted']

    # Load model from HuggingFace Hub
    tokenizer = AutoTokenizer.from_pretrained(path_to_model)
    model = AutoModel.from_pretrained(path_to_model)

    # Tokenize sentences
    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Perform pooling
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    # Normalize embeddings
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

    print("Sentence embeddings:")

    embeddings = sentence_embeddings.numpy().tolist()

    print(embeddings)

    return JSONResponse(content=embeddings)


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)
    # gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

