**Example 1: 获取单个合规组下的RDB关系数据库分类分级数据资产**



Input: 

```
tccli dsgc DescribeDSPARDBDataAssetByComplianceId --cli-unfold-argument  \
    --DspaId dspa-00001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Stats": {
            "DataAssetType": 0,
            "TotalDbCnt": 0,
            "TotalTableCnt": 0,
            "SensitiveCategoryCnt": 0,
            "SensitiveFieldCnt": 0,
            "SensitiveLevel": [
                {
                    "LevelId": 0,
                    "LevelCnt": 0,
                    "LevelRiskName": "abc",
                    "LevelRiskScore": 0
                }
            ],
            "SensitiveDbCnt": 0,
            "SensitiveTableCnt": 0,
            "TotalFieldCnt": 0,
            "CategoryDistributed": [
                {
                    "CategoryId": 0,
                    "CategoryName": "abc",
                    "Count": 1,
                    "CategoryFullPath": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

