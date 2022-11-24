import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

test = pd.read_csv("test/testdata/test.csv")
for x in test["tweet"]