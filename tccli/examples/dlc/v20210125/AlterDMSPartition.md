**Example 1: 修改表分区**

修改表分区

Input: 

```
tccli dlc AlterDMSPartition --cli-unfold-argument  \
    --CurrentValues abc \
    --Partition.Sds.OutputFormat abc \
    --Partition.Sds.SortCols.Col abc \
    --Partition.Sds.SortCols.Order 0 \
    --Partition.Sds.InputFormat abc \
    --Partition.Sds.SerdeLib abc \
    --Partition.Sds.Cols.0.Name abc \
    --Partition.Sds.Cols.0.BizParams.0.Value abc \
    --Partition.Sds.Cols.0.BizParams.0.Key abc \
    --Partition.Sds.Cols.0.IsPartition True \
    --Partition.Sds.Cols.0.Params.0.Value abc \
    --Partition.Sds.Cols.0.Params.0.Key abc \
    --Partition.Sds.Cols.0.Position 0 \
    --Partition.Sds.Cols.0.Type abc \
    --Partition.Sds.Cols.0.Description abc \
    --Partition.Sds.Compressed True \
    --Partition.Sds.Params.0.Value abc \
    --Partition.Sds.Params.0.Key abc \
    --Partition.Sds.Location abc \
    --Partition.Sds.NumBuckets 0 \
    --Partition.Sds.SerdeParams.0.Value abc \
    --Partition.Sds.SerdeParams.0.Key abc \
    --Partition.Sds.SerdeName abc \
    --Partition.Sds.StoredAsSubDirectories True \
    --Partition.Sds.BucketCols abc \
    --Partition.Name abc \
    --Partition.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partition.DataVersion 0 \
    --Partition.RecordCount 0 \
    --Partition.TableName abc \
    --Partition.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partition.Values abc \
    --Partition.DatabaseName abc \
    --Partition.Params.0.Value abc \
    --Partition.Params.0.Key abc \
    --Partition.SchemaName abc \
    --Partition.StorageSize 0 \
    --Partition.CreateTime 2020-09-22T00:00:00+00:00 \
    --CurrentTableName abc \
    --CurrentDbName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

