from CardoExecutor.Common.CardoContext import CardoContext
from CardoExecutor.Common.CardoDataFrame import CardoDataFrame
from CardoExecutor.Contract.IStep import IStep

class CsvFileWriter(IStep):
	def __init__(self, name):
		self.name = name

	def process(self, cardo_context, cardo_dataframe):
		cardo_dataframe.to_csv(self.name)
