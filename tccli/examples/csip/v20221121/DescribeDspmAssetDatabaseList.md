**Example 1: 查询资产数据库信息**



Input: 

```
tccli csip DescribeDspmAssetDatabaseList --cli-unfold-argument  \
    --AssetId cdb-21e9sdha \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DataSet": [
            {
                "AssetId": "cdb-c2thbt00",
                "DbName": "test_db",
                "TableCount": 10,
                "SensitiveTableCount": 5,
                "RuleIds": [
                    5800
                ],
                "RuleNames": [
                    "姓名"
                ]
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

