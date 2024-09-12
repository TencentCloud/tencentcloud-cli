**Example 1: 修改表**



Input: 

```
tccli dlc AlterDMSTable --cli-unfold-argument  \
    --PartitionKeys.0.Name abc \
    --PartitionKeys.0.BizParams.0.Value abc \
    --PartitionKeys.0.BizParams.0.Key abc \
    --PartitionKeys.0.IsPartition True \
    --PartitionKeys.0.Params.0.Value abc \
    --PartitionKeys.0.Params.0.Key abc \
    --PartitionKeys.0.Position 0 \
    --PartitionKeys.0.Type abc \
    --PartitionKeys.0.Description abc \
    --RecordCount 0 \
    --CurrentName abc \
    --Sds.OutputFormat abc \
    --Sds.SortCols.Col col1 \
    --Sds.SortCols.Order 0 \
    --Sds.InputFormat abc \
    --Sds.SerdeLib abc \
    --Sds.Cols.0.Name abc \
    --Sds.Cols.0.BizParams.0.Value abc \
    --Sds.Cols.0.BizParams.0.Key abc \
    --Sds.Cols.0.IsPartition True \
    --Sds.Cols.0.Params.0.Value abc \
    --Sds.Cols.0.Params.0.Key abc \
    --Sds.Cols.0.Position 0 \
    --Sds.Cols.0.Type abc \
    --Sds.Cols.0.Description abc \
    --Sds.Compressed True \
    --Sds.Params.0.Value abc \
    --Sds.Params.0.Key abc \
    --Sds.Location cosn://abc \
    --Sds.NumBuckets 0 \
    --Sds.SerdeParams.0.Value abc \
    --Sds.SerdeParams.0.Key abc \
    --Sds.SerdeName abc \
    --Sds.StoredAsSubDirectories True \
    --Sds.BucketCols abc \
    --StructUpdateTime 2020-09-22T00:00:00+00:00 \
    --DataUpdateTime 2020-09-22T00:00:00+00:00 \
    --LastAccessTime 2020-09-22T00:00:00+00:00 \
    --StorageSize 0 \
    --CurrentDbName db \
    --ViewExpandedText abc \
    --Asset.Description abc \
    --Asset.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Asset.DataVersion 0 \
    --Asset.BizParams.0.Value abc \
    --Asset.BizParams.0.Key abc \
    --Asset.OwnerAccount abc \
    --Asset.CreateTime 2020-09-22T00:00:00+00:00 \
    --Asset.Catalog abc \
    --Asset.Params.0.Value abc \
    --Asset.Params.0.Key abc \
    --Asset.PermValues.0.Value abc \
    --Asset.PermValues.0.Key abc \
    --Asset.Owner abc \
    --Asset.DatasourceId 0 \
    --Asset.Guid abc \
    --Asset.Id 0 \
    --Asset.Name abc \
    --LifeTime 0 \
    --ViewOriginalText abc \
    --Type abc \
    --DbName abc \
    --Columns.0.Name abc \
    --Columns.0.BizParams.0.Value abc \
    --Columns.0.BizParams.0.Key abc \
    --Columns.0.IsPartition True \
    --Columns.0.Params.0.Value abc \
    --Columns.0.Params.0.Key abc \
    --Columns.0.Position 0 \
    --Columns.0.Type abc \
    --Columns.0.Description abc \
    --Partitions.0.Sds.OutputFormat abc \
    --Partitions.0.Sds.SortCols.Col col1 \
    --Partitions.0.Sds.SortCols.Order 0 \
    --Partitions.0.Sds.InputFormat abc \
    --Partitions.0.Sds.SerdeLib abc \
    --Partitions.0.Sds.Cols.0.Name abc \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value abc \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key abc \
    --Partitions.0.Sds.Cols.0.IsPartition True \
    --Partitions.0.Sds.Cols.0.Params.0.Value abc \
    --Partitions.0.Sds.Cols.0.Params.0.Key abc \
    --Partitions.0.Sds.Cols.0.Position 0 \
    --Partitions.0.Sds.Cols.0.Type abc \
    --Partitions.0.Sds.Cols.0.Description abc \
    --Partitions.0.Sds.Compressed True \
    --Partitions.0.Sds.Params.0.Value abc \
    --Partitions.0.Sds.Params.0.Key abc \
    --Partitions.0.Sds.Location abc \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.SerdeParams.0.Value abc \
    --Partitions.0.Sds.SerdeParams.0.Key abc \
    --Partitions.0.Sds.SerdeName abc \
    --Partitions.0.Sds.StoredAsSubDirectories True \
    --Partitions.0.Sds.BucketCols abc \
    --Partitions.0.Name abc \
    --Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.DataVersion 0 \
    --Partitions.0.RecordCount 0 \
    --Partitions.0.TableName abc \
    --Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.Values abc \
    --Partitions.0.DatabaseName abc \
    --Partitions.0.Params.0.Value abc \
    --Partitions.0.Params.0.Key abc \
    --Partitions.0.SchemaName abc \
    --Partitions.0.StorageSize 0 \
    --Partitions.0.CreateTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

