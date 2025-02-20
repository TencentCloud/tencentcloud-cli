**Example 1: 修改表**



Input: 

```
tccli dlc AlterDMSTable --cli-unfold-argument  \
    --CurrentName table3 \
    --CurrentDbName database1 \
    --Asset.Name table3 \
    --Asset.Catalog DataLakeCatalog \
    --Asset.Description alter description \
    --Asset.Params.0.Key param1 \
    --Asset.Params.0.Value default param \
    --Asset.BizParams.0.Key bizparam1 \
    --Asset.BizParams.0.Value default bizparam \
    --Type EXTERNAL \
    --DbName database1 \
    --Sds.Location cons://******** \
    --Sds.InputFormat org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat \
    --Sds.OutputFormat org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat \
    --Sds.NumBuckets 0 \
    --Sds.Compressed False \
    --Sds.StoredAsSubDirectories False \
    --Sds.SerdeLib org.apache.hadoop.hive.serde2.OpenCSVSerde \
    --Sds.SerdeName serde1 \
    --Sds.BucketCols col1 \
    --Sds.SerdeParams.0.Key serde \
    --Sds.SerdeParams.0.Value 1 \
    --Sds.Params.0.Key param1 \
    --Sds.Params.0.Value default param \
    --Columns.0.Name id \
    --Columns.0.Description alter col \
    --Columns.0.Type int \
    --Columns.0.IsPartition True \
    --PartitionKeys.0.Name dt \
    --PartitionKeys.0.Description default description \
    --PartitionKeys.0.Type int \
    --PartitionKeys.0.Position 1 \
    --PartitionKeys.0.BizParams.0.Key None \
    --PartitionKeys.0.BizParams.0.Value None \
    --PartitionKeys.0.IsPartition True \
    --Partitions.0.DatabaseName database1 \
    --Partitions.0.TableName table3 \
    --Partitions.0.DataVersion 1 \
    --Partitions.0.Name dt2 \
    --Partitions.0.Values 1 \
    --Partitions.0.Params.0.Key None \
    --Partitions.0.Params.0.Value None \
    --Partitions.0.Sds.Location cosn://******** \
    --Partitions.0.Sds.InputFormat org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat \
    --Partitions.0.Sds.OutputFormat org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.Compressed False \
    --Partitions.0.Sds.StoredAsSubDirectories None \
    --Partitions.0.Sds.SerdeLib org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe \
    --Partitions.0.Sds.SerdeName serde2 \
    --Partitions.0.Sds.BucketCols col2 \
    --Partitions.0.Sds.SerdeParams.0.Key None \
    --Partitions.0.Sds.SerdeParams.0.Value None \
    --Partitions.0.Sds.Params.0.Key param3 \
    --Partitions.0.Sds.Params.0.Value default param \
    --Partitions.0.Sds.SortCols.Col None \
    --Partitions.0.Sds.SortCols.Order None \
    --Partitions.0.Sds.Cols.0.Name column1 \
    --Partitions.0.Sds.Cols.0.Description default column \
    --Partitions.0.Sds.Cols.0.Type int \
    --Partitions.0.Sds.Cols.0.Position 1 \
    --Partitions.0.Sds.Cols.0.Params.0.Key param1 \
    --Partitions.0.Sds.Cols.0.Params.0.Value default param \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key bizparam1 \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value default bizparam \
    --Partitions.0.Sds.Cols.0.IsPartition False \
    --Name table3 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-237bfeec9223"
    }
}
```

