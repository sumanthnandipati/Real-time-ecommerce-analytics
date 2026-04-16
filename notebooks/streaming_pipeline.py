# Real-Time E-commerce Streaming Pipeline

from pyspark.sql.functions import col, window, sum

# Read streaming data (example)
df = spark.readStream.format("json").load("/FileStore/events")

# Revenue aggregation
revenue_df = df.filter(col("event_type") == "purchase") \
    .groupBy(window(col("timestamp"), "5 minutes")) \
    .agg(sum("price").alias("purchase_revenue"))

# Write to Gold table
revenue_df.writeStream \
    .format("delta") \
    .outputMode("complete") \
    .option("checkpointLocation", "/tmp/checkpoints/revenue") \
    .table("gold_purchase_revenue")
