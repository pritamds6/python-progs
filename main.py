#from pyspark import SparkSession
import pandas as pd
print("hello")
df=pd.read_csv('test.csv')
print(df.to_string()) 
print("New Feature added test1")

#spark=SparkSession.builder.appname('Practise').getOrCreate()

