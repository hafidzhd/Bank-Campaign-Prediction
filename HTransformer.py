#Class to select dataset with condition
class SelectColumnsCondition():
    def __init__(self, columns=None, value=None) :
        self.columns = columns
        self.value= value

    def transform(self, X, **transform_params):
        cpy_df = X.copy()
        df_fin = cpy_df.drop(cpy_df[cpy_df[self.columns] == self.value ].index).reset_index(drop=True)
        return df_fin

    def fit(self, X, y=None, **fit_params):
        return self 

#Class to select column from dataset
class SelectColumn():
    def __init__(self, columns=None) :
        self.columns = columns

    def transform(self, X, **transform_params):
        cpy_df = X.copy()
        df_fin = cpy_df[list(self.columns)]
        return df_fin

    def fit(self, X, y=None, **fit_params):
        return self 

