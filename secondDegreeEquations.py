import numpy as np
import fastapi 
from fastapi import FastAPI 

app = FastAPI()

@app.put("/items/{item_id1},{item_id2},{item_id3}")

def kök_bul(item_id1: float, item_id2: float, item_id3:float):
    
    disc = (item_id2**2) - (4 * item_id1 * item_id3)
    x1 = (- item_id2 + np.sqrt(disc))/(2*item_id1)
    x2 = (- item_id2 - np.sqrt(disc))/(2*item_id1)

    print("\nEquation:", item_id1, "x^2 +", item_id2, " x + ", item_id3)
    print("Roots : \n", "x1 = ", x1, "x2 = ", x2)

    return None 

kök_bul(1. , -1., -12.)
