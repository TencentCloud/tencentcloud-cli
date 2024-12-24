**Example 1: 概览页**

概览页

Input: 

```
tccli dsgc DescribeDSPAESDataAssetByComplianceId --cli-unfold-argument  \
    --DspaId dspa-acfd125b \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Stats": {
            "DataAssetType": 1,
            "SensitiveIndexCnt": 3,
            "TotalIndexCnt": 15,
            "SensitiveFieldCnt": 5,
            "TotalFieldCnt": 60,
            "SensitiveCategoryCnt": 2,
            "SensitiveLevel": [
                {
                    "LevelId": 102,
                    "LevelCnt": 2,
                    "LevelRiskName": "高",
                    "LevelRiskScore": 10
                }
            ],
            "CategoryDistributed": [
                {
                    "CategoryId": 103,
                    "CategoryName": "个人基本信息",
                    "Count": 1,
                    "CategoryFullPath": "[\"个人基本信息\"]"
                }
            ]
        },
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

