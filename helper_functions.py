def missing_values(df):
    return df.isnull().sum()

def dataset_shape(df):
    return df.shape

def duplicate_rows(df):
    return df.duplicated().sum()