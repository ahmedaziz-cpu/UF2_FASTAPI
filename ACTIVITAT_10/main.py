from fastapi import FastAPI
from typing import List

import options_sch
#from pydantic import BaseModel
import read
#import read




app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Benvingut a fastapi"}


# Mètode per extreure les 5 opcions i podre-les mostrar a la llista de selecció d'opcions del penjat
@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_options():
    return options_sch.options_schema(read.read_db())


# En aquesta consulta get ecaldrà que el frontend envii a {option} la opció seleccionada en la llista del joc
@app.get("/penjat/tematica/{option}", response_model=List[dict])
async def get_word(option: str):
    word = options_sch.options_schema(read.read_word_db(option))
    print("")
    print("IMPRESSIÓ WORD del mètode GET_WORD")
    print(type(word))
    print(word)

    return word
