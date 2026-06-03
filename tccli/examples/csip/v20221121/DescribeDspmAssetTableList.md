**Example 1: 查询资产表信息**



Input: 

```
tccli csip DescribeDspmAssetTableList --cli-unfold-argument  \
    --AssetId cdb-21e9sdha \
    --DbName test_db \
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
                "SchemaName": "test_schema",
                "TableName": "test_tb",
                "FieldCount": 10,
                "SensitiveFieldCount": 5,
                "RuleIds": [
                    5800
                ],
                "RuleNames": [
                    "姓名"
                ],
                "CategoryIds": [
                    356
                ],
                "CategoryNames": [
                    "姓名"
                ]
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

