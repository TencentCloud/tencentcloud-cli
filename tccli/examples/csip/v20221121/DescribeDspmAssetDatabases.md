**Example 1: 查询Dspm资产数据库列表**



Input: 

```
tccli csip DescribeDspmAssetDatabases --cli-unfold-argument  \
    --AssetId cdb-c2thbt00
```

Output: 
```
{
    "Response": {
        "Items": [
            "testdatabase1",
            "testdatabase2"
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

