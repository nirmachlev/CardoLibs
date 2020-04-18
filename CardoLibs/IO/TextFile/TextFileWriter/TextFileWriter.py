from CardoExecutor.Common.CardoContext import CardoContext
from CardoExecutor.Common.CardoDataFrame import CardoDataFrame
from CardoExecutor.Contract.IStep import IStep


class TextFileWriter(IStep):
	def __init__(self, name):
		self.name = name

	def process(self, cardo_context, cardo_dataframe):
		with open(self.name, "w") as outFile:
			outFile.write(str(cardo_dataframe))