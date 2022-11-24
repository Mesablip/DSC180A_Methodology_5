import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

test = pd.read_csv("test/testdata/test.csv")
accurate = []
for x, y in zip(test["tweet"], test["label"]):
    ents = nlp(x).ents
    if yin ents:
        accurate.append(1)
    else:
        accurate.append(0)
print(accurate)