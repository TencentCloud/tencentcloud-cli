**Example 1: DMS元数据创建库**



Input: 

```
tccli dlc CreateDMSDatabase --cli-unfold-argument  \
    --Asset.Description api 测试库 \
    --Asset.ModifiedTime 2023-07-24T15:26:30+00:00 \
    --Asset.DataVersion 0 \
    --Asset.BizParams.0.Value  \
    --Asset.BizParams.0.Key  \
    --Asset.OwnerAccount 100016321234396 \
    --Asset.CreateTime 2023-07-24T15:26:30+00:00 \
    --Asset.Catalog  \
    --Asset.Params.0.Value  \
    --Asset.Params.0.Key  \
    --Asset.PermValues.0.Value  \
    --Asset.PermValues.0.Key  \
    --Asset.Owner 100016334432227396 \
    --Asset.DatasourceId 100 \
    --Asset.Guid 123-456-789 \
    --Asset.Id 1 \
    --Asset.Name api_test \
    --SchemaName api_test \
    --Location cosn://api_test \
    --Name api_test \
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

