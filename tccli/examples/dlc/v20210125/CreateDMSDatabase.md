**Example 1: DMS元数据创建库**



Input: 

```
tccli dlc CreateDMSDatabase --cli-unfold-argument  \
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
    --SchemaName test \
    --Location cosn://
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

