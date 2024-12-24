**Example 1: 获取单个合规组下的RDB关系数据库分类分级数据资产**



Input: 

```
tccli dsgc DescribeDSPARDBDataAssetByComplianceId --cli-unfold-argument  \
    --DspaId dspa-89asd23n \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Stats": {
            "DataAssetType": 0,
            "TotalDbCnt": 2,
            "TotalTableCnt": 5,
            "SensitiveCategoryCnt": 1,
            "SensitiveFieldCnt": 6,
            "SensitiveLevel": [
                {
                    "LevelId": 101,
                    "LevelCnt": 2,
                    "LevelRiskName": "高",
                    "LevelRiskScore": 10
                }
            ],
            "SensitiveDbCnt": 2,
            "SensitiveTableCnt": 2,
            "TotalFieldCnt": 8,
            "CategoryDistributed": [
                {
                    "CategoryId": 103,
                    "CategoryName": "个人基本信息",
                    "Count": 5,
                    "CategoryFullPath": "基本信息/个人基本信息"
                }
            ]
        },
        "RequestId": "1f1765cf-c01a-4a93-95b2-99108f4aa04f"
    }
}
```

