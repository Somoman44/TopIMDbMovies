import pandas as pd
from sklearn.base import BaseEstimator,TransformerMixin
import category_encoders as ce
class ExplodedLooEcoder(BaseEstimator,TransformerMixin):
    def __init__(self,col):
        self.col = col
        self.encoder = None
        
    def fit(self,X,y):
        X_fit =X.copy()
        X_fit['target'] = y
        X_exploded = X_fit.explode(self.col)
        self.encoder = ce.LeaveOneOutEncoder(cols=[self.col])
        self.encoder.fit(X_exploded[self.col],X_exploded['target'])
        return self
    
    def transform(self,X):
        X_exploded = X.explode(self.col)
        X_encoded = self.encoder.transform(X_exploded[self.col])
        agg = X_encoded.groupby(X_encoded.index)[self.col].mean()
        X_agg = agg.to_frame(f'foo_{self.col}')
        X_transformed = pd.merge(X,X_agg,how='left',left_index=True,right_index=True)
        X_transformed.drop(columns=[self.col],inplace=True)
        return X_transformed
   