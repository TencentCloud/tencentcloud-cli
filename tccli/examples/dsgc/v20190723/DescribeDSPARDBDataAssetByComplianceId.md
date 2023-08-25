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
            "SensitiveDbCnt": 3,
            "SensitiveLevel": [
                {
                    "LevelCnt": 10,
                    "LevelRiskName": "S2",
                    "LevelRiskScore": 10,
                    "LevelId": 1
                }
            ],
            "CategoryDistributed": [
                {
                    "Count": 1,
                    "CategoryId": 0,
                    "CategoryName": "xx"
                }
            ],
            "TotalFieldCnt": 50,
            "SensitiveCategoryCnt": 6,
            "TotalTableCnt": 20,
            "TotalDbCnt": 5,
            "SensitiveFieldCnt": 20,
            "SensitiveTableCnt": 10,
            "DataAssetType": 0
        },
        "RequestId": "xx"
    }
}
```

