**Example 1: DMS元数据更新库**



Input: 

```
tccli dlc AlterDMSDatabase --cli-unfold-argument  \
    --CurrentName xx \
    --SchemaName xx \
    --Location xx \
    --Asset.Description xx \
    --Asset.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Asset.DataVersion 1 \
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
    --Asset.DatasourceId 1 \
    --Asset.Guid xx \
    --Asset.Id 1 \
    --Asset.Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

