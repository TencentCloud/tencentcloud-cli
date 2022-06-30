**Example 1: 修改表分区**

修改表分区

Input: 

```
tccli dlc AlterDMSPartition --cli-unfold-argument  \
    --CurrentValues xx \
    --Partition.Sds.OutputFormat xx \
    --Partition.Sds.SortCols.Col xx \
    --Partition.Sds.SortCols.Order 0 \
    --Partition.Sds.InputFormat xx \
    --Partition.Sds.SerdeLib xx \
    --Partition.Sds.Cols.0.Name xx \
    --Partition.Sds.Cols.0.BizParams.0.Value xx \
    --Partition.Sds.Cols.0.BizParams.0.Key xx \
    --Partition.Sds.Cols.0.IsPartition True \
    --Partition.Sds.Cols.0.Params.0.Value xx \
    --Partition.Sds.Cols.0.Params.0.Key xx \
    --Partition.Sds.Cols.0.Position 0 \
    --Partition.Sds.Cols.0.Type xx \
    --Partition.Sds.Cols.0.Description xx \
    --Partition.Sds.Compressed True \
    --Partition.Sds.Params.0.Value xx \
    --Partition.Sds.Params.0.Key xx \
    --Partition.Sds.Location xx \
    --Partition.Sds.NumBuckets 0 \
    --Partition.Sds.SerdeParams.0.Value xx \
    --Partition.Sds.SerdeParams.0.Key xx \
    --Partition.Sds.SerdeName xx \
    --Partition.Sds.StoredAsSubDirectories True \
    --Partition.Sds.BucketCols xx \
    --Partition.Name xx \
    --Partition.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partition.DataVersion 0 \
    --Partition.RecordCount 0 \
    --Partition.TableName xx \
    --Partition.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partition.Values xx \
    --Partition.DatabaseName xx \
    --Partition.Params.0.Value xx \
    --Partition.Params.0.Key xx \
    --Partition.SchemaName xx \
    --Partition.StorageSize 0 \
    --Partition.CreateTime 2020-09-22T00:00:00+00:00 \
    --CurrentTableName xx \
    --CurrentDbName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

