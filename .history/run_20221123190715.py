import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

test = pd.read_csv("test/testdata/test.csv")
accurate = []
for x in test["tweet"]:
    ents = nlp(x).ents
    if x["label"] in 