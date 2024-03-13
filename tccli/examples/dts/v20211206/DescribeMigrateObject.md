**Example 1: 查看迁移库表**



Input: 

```
tccli dts DescribeMigrateObject --cli-unfold-argument  \
    --JobId dts-mcl8vzmy \
    --Pagination enabled \
    --Limit 10 \
    --Offset 0 \
    --ObjectFilter  \
    --ObjectType table \
    --ObjectPath test
```

Output: 
```
{
    "Response": {
        "IsLeaf": 1,
        "ObjectList": [],
        "RequestId": "8dc98b40-bfe3-11ec-8442-cb2a72d60b79",
        "TotalCount": 0
    }
}
```

