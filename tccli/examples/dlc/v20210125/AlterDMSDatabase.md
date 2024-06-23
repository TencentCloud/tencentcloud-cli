**Example 1: DMS元数据更新库**



Input: 

```
tccli dlc AlterDMSDatabase --cli-unfold-argument  \
    --CurrentName abc \
    --SchemaName abc \
    --Location abc \
    --Asset.Id 0 \
    --Asset.Name abc \
    --Asset.Guid abc \
    --Asset.Catalog abc \
    --Asset.Description abc \
    --Asset.Owner abc \
    --Asset.OwnerAccount abc \
    --Asset.PermValues.0.Key abc \
    --Asset.PermValues.0.Value abc \
    --Asset.Params.0.Key abc \
    --Asset.Params.0.Value abc \
    --Asset.BizParams.0.Key abc \
    --Asset.BizParams.0.Value abc \
    --Asset.DataVersion 0 \
    --Asset.CreateTime 2020-09-22T00:00:00+00:00 \
    --Asset.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Asset.DatasourceId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

