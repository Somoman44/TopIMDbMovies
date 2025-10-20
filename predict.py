import joblib
import pandas as pd
from src.transformers.custom_transformer import ExplodedLooEcoder 

file = 'models/pipeline.joblib'
predict_rating = joblib.load(file)

#'Votes','Meta Score','Tags', 'Director','Writers','Stars'
sample = pd.DataFrame({
    'Votes':[142000],
    'Meta Score':[80],
    'Director':['J.J Abrams'],
    'Tags':[['Action','Space Opera','Adventure','Sci-fi']],
    'Writers':[['J.J Abrams','Lawrence Kasdan','Michael Arndt']],
})

print(predict_rating.predict(sample))