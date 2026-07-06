**Example 1: 查询资产数据库信息**



Input: 

```
tccli csip DescribeDspmAssetDatabaseList --cli-unfold-argument  \
    --AssetId cdb-l8hhoqwd
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "AssetId": "cdb-l8hhoqwd",
                "CategoryDetails": [
                    {
                        "CategoryId": 356,
                        "CategoryName": "个人信息",
                        "RuleSet": [
                            {
                                "LevelId": 10,
                                "LevelScore": 1,
                                "RuleId": 5836,
                                "RuleName": "QQ"
                            }
                        ]
                    }
                ],
                "CategoryIds": [
                    355
                ],
                "CategoryNames": [
                    "个人敏感信息"
                ],
                "DbName": "dspm01",
                "RuleIds": [
                    5800
                ],
                "RuleNames": [
                    "姓名"
                ],
                "SensitiveTableCount": 1,
                "TableCount": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "cac6252a-7788-4606-8431-ab7e57432f72"
    }
}
```

