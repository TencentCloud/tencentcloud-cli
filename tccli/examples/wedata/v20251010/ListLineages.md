**Example 1: 获取血缘列表**



Input: 

```
tccli wedata ListLineages --cli-unfold-argument  \
    --ResourceName DataLakeCatalog.db_lcl.person_ice_part \
    --ResourceType TABLE \
    --Direction OUTPUT \
    --Page.PageSize 1 \
    --Page.PageNumber 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "TotalCount": "0"
        },
        "RequestId": "1f9f49ef-87df-4649-8d2c-b6c6caa768b0"
    }
}
```

