**Example 1: 修改表分区**

修改表分区

Input: 

```
tccli dlc AlterDMSPartition --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --CurrentDbName database1 \
    --CurrentTableName table2 \
    --CurrentValues 1 \
    --Partition.DatabaseName database1 \
    --Partition.TableName table2 \
    --Partition.DataVersion 1 \
    --Partition.Name id \
    --Partition.Values 2 \
    --Partition.Params.0.Key param1 \
    --Partition.Params.0.Value default param \
    --Partition.Sds.Location cosn://******** \
    --Partition.Sds.InputFormat org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat \
    --Partition.Sds.OutputFormat org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat \
    --Partition.Sds.NumBuckets 0 \
    --Partition.Sds.Compressed False \
    --Partition.Sds.StoredAsSubDirectories False \
    --Partition.Sds.SerdeLib org.apache.hadoop.hive.serde2.OpenCSVSerde \
    --Partition.Sds.SerdeName serde1 \
    --Partition.Sds.SerdeParams.0.Key separatorChar \
    --Partition.Sds.SerdeParams.0.Value \t \
    --Partition.Sds.Params.0.Key param2 \
    --Partition.Sds.Params.0.Value default param
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

