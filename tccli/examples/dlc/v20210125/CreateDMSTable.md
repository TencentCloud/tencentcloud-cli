**Example 1: 创建表**

创建表

Input: 

```
tccli dlc CreateDMSTable --cli-unfold-argument  \
    --PartitionKeys.0.Name xx \
    --PartitionKeys.0.BizParams.0.Value xx \
    --PartitionKeys.0.BizParams.0.Key xx \
    --PartitionKeys.0.IsPartition True \
    --PartitionKeys.0.Params.0.Value xx \
    --PartitionKeys.0.Params.0.Key xx \
    --PartitionKeys.0.Position 0 \
    --PartitionKeys.0.Type xx \
    --PartitionKeys.0.Description xx \
    --RecordCount 0 \
    --Sds.OutputFormat xx \
    --Sds.SortCols.Col xx \
    --Sds.SortCols.Order 0 \
    --Sds.InputFormat xx \
    --Sds.SerdeLib xx \
    --Sds.Cols.0.Name xx \
    --Sds.Cols.0.BizParams.0.Value xx \
    --Sds.Cols.0.BizParams.0.Key xx \
    --Sds.Cols.0.IsPartition True \
    --Sds.Cols.0.Params.0.Value xx \
    --Sds.Cols.0.Params.0.Key xx \
    --Sds.Cols.0.Position 0 \
    --Sds.Cols.0.Type xx \
    --Sds.Cols.0.Description xx \
    --Sds.Compressed True \
    --Sds.Params.0.Value xx \
    --Sds.Params.0.Key xx \
    --Sds.Location xx \
    --Sds.NumBuckets 0 \
    --Sds.SerdeParams.0.Value xx \
    --Sds.SerdeParams.0.Key xx \
    --Sds.SerdeName xx \
    --Sds.StoredAsSubDirectories True \
    --Sds.BucketCols xx \
    --StructUpdateTime 2020-09-22T00:00:00+00:00 \
    --DataUpdateTime 2020-09-22T00:00:00+00:00 \
    --LastAccessTime 2020-09-22T00:00:00+00:00 \
    --StorageSize 0 \
    --Asset.Description xx \
    --Asset.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Asset.DataVersion 0 \
    --Asset.BizParams.0.Value xx \
    --Asset.BizParams.0.Key xx \
    --Asset.OwnerAccount xx \
    --Asset.CreateTime 2020-09-22T00:00:00+00:00 \
    --Asset.Catalog xx \
    --Asset.Params.0.Value xx \
    --Asset.Params.0.Key xx \
    --Asset.PermValues.0.Value xx \
    --Asset.PermValues.0.Key xx \
    --Asset.Owner xx \
    --Asset.DatasourceId 0 \
    --Asset.Guid xx \
    --Asset.Id 0 \
    --Asset.Name xx \
    --ViewExpandedText xx \
    --LifeTime 0 \
    --ViewOriginalText xx \
    --Type xx \
    --DbName xx \
    --Columns.0.Name xx \
    --Columns.0.BizParams.0.Value xx \
    --Columns.0.BizParams.0.Key xx \
    --Columns.0.IsPartition True \
    --Columns.0.Params.0.Value xx \
    --Columns.0.Params.0.Key xx \
    --Columns.0.Position 0 \
    --Columns.0.Type xx \
    --Columns.0.Description xx \
    --Partitions.0.Sds.OutputFormat xx \
    --Partitions.0.Sds.SortCols.Col xx \
    --Partitions.0.Sds.SortCols.Order 0 \
    --Partitions.0.Sds.InputFormat xx \
    --Partitions.0.Sds.SerdeLib xx \
    --Partitions.0.Sds.Cols.0.Name xx \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value xx \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key xx \
    --Partitions.0.Sds.Cols.0.IsPartition True \
    --Partitions.0.Sds.Cols.0.Params.0.Value xx \
    --Partitions.0.Sds.Cols.0.Params.0.Key xx \
    --Partitions.0.Sds.Cols.0.Position 0 \
    --Partitions.0.Sds.Cols.0.Type xx \
    --Partitions.0.Sds.Cols.0.Description xx \
    --Partitions.0.Sds.Compressed True \
    --Partitions.0.Sds.Params.0.Value xx \
    --Partitions.0.Sds.Params.0.Key xx \
    --Partitions.0.Sds.Location xx \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.SerdeParams.0.Value xx \
    --Partitions.0.Sds.SerdeParams.0.Key xx \
    --Partitions.0.Sds.SerdeName xx \
    --Partitions.0.Sds.StoredAsSubDirectories True \
    --Partitions.0.Sds.BucketCols xx \
    --Partitions.0.Name xx \
    --Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.DataVersion 0 \
    --Partitions.0.RecordCount 0 \
    --Partitions.0.TableName xx \
    --Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.Values xx \
    --Partitions.0.DatabaseName xx \
    --Partitions.0.Params.0.Value xx \
    --Partitions.0.Params.0.Key xx \
    --Partitions.0.SchemaName xx \
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

