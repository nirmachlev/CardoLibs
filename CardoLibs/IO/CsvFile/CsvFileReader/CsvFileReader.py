from CardoExecutor.Common.CardoContext import CardoContext
from CardoExecutor.Common.CardoDataFrame import CardoDataFrame
from CardoExecutor.Contract.IStep import IStep
import pandas as pd


class CsvFileReader(IStep):
    def __init__(self, name):
        self.name = name

    def process(self, cardo_context, cardo_dataframe=None):
        return pd.read_csv(self.name)
