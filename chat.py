import torch
import warnings
from module import Khaosz, Transformer, Config

warnings.filterwarnings("ignore")

def chat():
    model = Khaosz("params")
    model = model.to(device='cuda', dtype=torch.float16)
    histroy = []
    with torch.no_grad():
        while True:
            query = input(">> ")
            if query == "!exit":
                break
            
            response_size = 0
            for response, histroy in model.stream_generate(
                query=query, 
                history=histroy,
                temperature=0.95,
                top_p=0.6,
                top_k=20
            ):
                print(response[response_size:], end="", flush=True)
                response_size = len(response)       
            print()

def show_parameter_size():
    cfg = Config("params/config.json")
    model = Transformer(cfg)
    print(f"parameter size: {model.parameter_size():,}")
    

if __name__ == "__main__":
    chat()