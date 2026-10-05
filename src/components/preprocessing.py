import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (StandardScaler,OneHotEncoder)
from config.paths import DATA_PATH
from config.paths import MODELS_PATH

import numpy as np
import joblib


def create_numerical_pipeline():
    return Pipeline(steps = [(
        'numerical scaler',
        StandardScaler(),
    ),
    ])

def create_categorical_pipeline():
    return Pipeline(steps = [(
        'Categorical Encoder',
        OneHotEncoder(),
    ),
    ])

def create_preprocessor(numerical, categorical):
    preprocessor = ColumnTransformer(
        transformers=[
            ('numerical',
             create_numerical_pipeline(),
             numerical),
        ('categorical',
         create_categorical_pipeline(),
         categorical),
        ])

    return preprocessor

def preprocess_data(
        X_train,X_test,
        numerical,
        categorical,

):


    preprocessor = create_preprocessor(numerical, categorical)
    X_train_preprocessed = preprocessor.fit_transform(X_train)
    X_test_preprocessed = preprocessor.fit_transform(X_test)
    joblib.dump(preprocessor,MODELS_PATH/ 'preprocessor.pkl')

    return (X_train_preprocessed, X_test_preprocessed, preprocessor)

def encode_target(y_train,y_test):
    mapping = {
        'N':0,
        'Y':1,
    }

    y_train =(y_train).map(mapping)
    y_test =(y_test).map(mapping)

    return (y_train,y_test)

