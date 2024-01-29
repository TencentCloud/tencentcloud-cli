**Example 1: 导入建表**

导入建表

Input: 

```
tccli wedata ImportTableData --cli-unfold-argument  \
    --ProjectId abc \
    --BucketName ff \
    --Description abc \
    --DatasourceId 0 \
    --TableRequest.MsType abc \
    --TableRequest.DbName abc \
    --TableRequest.Name abc \
    --TableRequest.Catalog abc \
    --TableRequest.Type abc \
    --TableRequest.Owner abc \
    --TableRequest.DatasourceId 0 \
    --TableRequest.OwnerAccount 0 \
    --TableRequest.NameCn abc \
    --TableRequest.Description abc \
    --TableRequest.PartitionType 0 \
    --TableRequest.LifeTime 1 \
    --TableRequest.StorageFormat abc \
    --TableRequest.ColumnDelimiter abc \
    --TableRequest.Columns.0.Position 0 \
    --TableRequest.Columns.0.Name abc \
    --TableRequest.Columns.0.Type abc \
    --TableRequest.Columns.0.Description abc \
    --TableRequest.Columns.0.IsPartition True \
    --TableRequest.Columns.0.BizParams.NameCn abc \
    --TableRequest.Columns.0.BizParams.NameEn abc \
    --TableRequest.Columns.0.BizParams.HasAdvancedConfig abc \
    --TableRequest.Columns.0.Precision 0 \
    --TableRequest.Columns.0.Scale 0 \
    --TableRequest.Columns.0.Params.Transform abc \
    --TableRequest.Columns.0.Params.TransformArgs abc \
    --TableRequest.PartitionKeys.0.Position 0 \
    --TableRequest.PartitionKeys.0.Name abc \
    --TableRequest.PartitionKeys.0.Type abc \
    --TableRequest.PartitionKeys.0.Description abc \
    --TableRequest.PartitionKeys.0.IsPartition True \
    --TableRequest.PartitionKeys.0.BizParams.NameCn abc \
    --TableRequest.PartitionKeys.0.BizParams.NameEn abc \
    --TableRequest.PartitionKeys.0.BizParams.HasAdvancedConfig abc \
    --TableRequest.PartitionKeys.0.Precision 0 \
    --TableRequest.PartitionKeys.0.Scale 0 \
    --TableRequest.PartitionKeys.0.Params.Transform abc \
    --TableRequest.PartitionKeys.0.Params.TransformArgs abc \
    --TableRequest.ConnectionType abc \
    --TableRequest.Namespace abc \
    --TableRequest.NameEn abc \
    --TableRequest.Sql abc \
    --TableRequest.BizParams.NameCn abc \
    --TableRequest.BizParams.NameEn abc \
    --TableRequest.BizParams.HasAdvancedConfig abc \
    --TableRequest.SchemaName abc \
    --NameCn abc \
    --ColumnDelimiter abc \
    --Privilege 0 \
    --HeaderLine 0 \
    --Escape abc \
    --Quote abc \
    --NullFormat abc \
    --FileEncode abc \
    --DatasourcePath abc \
    --StorageDataSourceType abc \
    --FileFormat abc \
    --ImportTableType abc \
    --MsType abc
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "abc"
    }
}
```

