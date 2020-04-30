from pyspark.sql.types import*

schma = StructType([StructField("person_id",StringType(),True),StructField("datetime",StringType(),True),StructField("floor_level",IntegerType(),True),StructField("building",StringType(),True)])

rdd1= sc.textFile("/home/vaibhav/Downloads/data.csv").map(lambda x:
x.encode("utf-8"))
head= rdd1.first()
rdd2= rdd1.filter(lambda x: x != head).map(lambda a:
a.split(",")).map(lambda a: [a[0],a[1],int(a[2]),a[3]])

df1 = spark.createDataFrame(rdd2,schma)
df1.write.json("/home/vaibhav/Downloads/result1.csv")
