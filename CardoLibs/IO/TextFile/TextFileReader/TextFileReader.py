from CardoExecutor.Common.CardoContext import CardoContext
from CardoExecutor.Common.CardoDataFrame import CardoDataFrame
from CardoExecutor.Contract.IStep import IStep
import pandas as pd

class TextFileReader(IStep):
	def __init__(self, name):
		self.name = name

	def process(self, cardo_context, cardo_dataframe=None):
		data = ""
		with open(self.name, "r") as outFile:
			value = int(outFile.read())
			data = pd.DataFrame(data=[{'value':value}],copy=True)
		return data