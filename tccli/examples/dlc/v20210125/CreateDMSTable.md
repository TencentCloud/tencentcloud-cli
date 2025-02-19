**Example 1: 创建表**

创建表

Input: 

```
tccli dlc CreateDMSTable --cli-unfold-argument  \
    --PartitionKeys.0.Name f_value \
    --PartitionKeys.0.BizParams.0.Value f_value \
    --PartitionKeys.0.BizParams.0.Key f_value \
    --PartitionKeys.0.IsPartition True \
    --PartitionKeys.0.Params.0.Value f_value \
    --PartitionKeys.0.Params.0.Key f_value \
    --PartitionKeys.0.Position 0 \
    --PartitionKeys.0.Type f_value \
    --PartitionKeys.0.Description f_value \
    --RecordCount 0 \
    --Sds.OutputFormat f_value \
    --Sds.SortCols.Col f_value \
    --Sds.SortCols.Order 0 \
    --Sds.InputFormat f_value \
    --Sds.SerdeLib f_value \
    --Sds.Cols.0.Name f_value \
    --Sds.Cols.0.BizParams.0.Value f_value \
    --Sds.Cols.0.BizParams.0.Key f_value \
    --Sds.Cols.0.IsPartition True \
    --Sds.Cols.0.Params.0.Value f_value \
    --Sds.Cols.0.Params.0.Key f_value \
    --Sds.Cols.0.Position 0 \
    --Sds.Cols.0.Type f_value \
    --Sds.Cols.0.Description f_value \
    --Sds.Compressed True \
    --Sds.Params.0.Value f_value \
    --Sds.Params.0.Key f_value \
    --Sds.Location f_value \
    --Sds.NumBuckets 0 \
    --Sds.SerdeParams.0.Value f_value \
    --Sds.SerdeParams.0.Key f_value \
    --Sds.SerdeName f_value \
    --Sds.StoredAsSubDirectories True \
    --Sds.BucketCols f_value \
    --StructUpdateTime 2020-09-22T00:00:00+00:00 \
    --DataUpdateTime 2020-09-22T00:00:00+00:00 \
    --LastAccessTime 2020-09-22T00:00:00+00:00 \
    --StorageSize 0 \
    --Asset.Description f_value \
    --Asset.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Asset.DataVersion 0 \
    --Asset.BizParams.0.Value f_value \
    --Asset.BizParams.0.Key f_value \
    --Asset.OwnerAccount f_value \
    --Asset.CreateTime 2020-09-22T00:00:00+00:00 \
    --Asset.Catalog f_value \
    --Asset.Params.0.Value f_value \
    --Asset.Params.0.Key f_value \
    --Asset.PermValues.0.Value f_value \
    --Asset.PermValues.0.Key f_value \
    --Asset.Owner f_value \
    --Asset.DatasourceId 0 \
    --Asset.Guid f_value \
    --Asset.Id 0 \
    --Asset.Name f_value \
    --ViewExpandedText f_value \
    --LifeTime 0 \
    --ViewOriginalText f_value \
    --Type f_value \
    --DbName f_value \
    --Columns.0.Name f_value \
    --Columns.0.BizParams.0.Value f_value \
    --Columns.0.BizParams.0.Key f_value \
    --Columns.0.IsPartition True \
    --Columns.0.Params.0.Value f_value \
    --Columns.0.Params.0.Key f_value \
    --Columns.0.Position 0 \
    --Columns.0.Type f_value \
    --Columns.0.Description f_value \
    --Partitions.0.Sds.OutputFormat f_value \
    --Partitions.0.Sds.SortCols.Col f_value \
    --Partitions.0.Sds.SortCols.Order 0 \
    --Partitions.0.Sds.InputFormat f_value \
    --Partitions.0.Sds.SerdeLib f_value \
    --Partitions.0.Sds.Cols.0.Name f_value \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value f_value \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key f_value \
    --Partitions.0.Sds.Cols.0.IsPartition True \
    --Partitions.0.Sds.Cols.0.Params.0.Value f_value \
    --Partitions.0.Sds.Cols.0.Params.0.Key f_value \
    --Partitions.0.Sds.Cols.0.Position 0 \
    --Partitions.0.Sds.Cols.0.Type f_value \
    --Partitions.0.Sds.Cols.0.Description f_value \
    --Partitions.0.Sds.Compressed True \
    --Partitions.0.Sds.Params.0.Value f_value \
    --Partitions.0.Sds.Params.0.Key f_value \
    --Partitions.0.Sds.Location f_value \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.SerdeParams.0.Value f_value \
    --Partitions.0.Sds.SerdeParams.0.Key f_value \
    --Partitions.0.Sds.SerdeName f_value \
    --Partitions.0.Sds.StoredAsSubDirectories True \
    --Partitions.0.Sds.BucketCols f_value \
    --Partitions.0.Name f_value \
    --Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.DataVersion 0 \
    --Partitions.0.RecordCount 0 \
    --Partitions.0.TableName f_value \
    --Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.Values f_value \
    --Partitions.0.DatabaseName f_value \
    --Partitions.0.Params.0.Value f_value \
    --Partitions.0.Params.0.Key f_value \
    --Partitions.0.SchemaName f_value \
    --Partitions.0.StorageSize 0 \
    --Partitions.0.CreateTime 2020-09-22T00:00:00+00:00 \
    --Name tb_test \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

