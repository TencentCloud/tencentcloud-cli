**Example 1: DMS元数据更新库**



Input: 

```
tccli dlc AlterDMSDatabase --cli-unfold-argument  \
    --CurrentName database1 \
    --SchemaName DataLakeCatalog \
    --Location cosn://********** \
    --Asset.Name database1 \
    --Asset.Catalog DataLakeCatalog \
    --Asset.Description alter description \
    --Asset.Params.0.Key param1 \
    --Asset.Params.0.Value default param \
    --Asset.BizParams.0.Key bizparam \
    --Asset.BizParams.0.Value default param
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-d91707f15fae"
    }
}
```

