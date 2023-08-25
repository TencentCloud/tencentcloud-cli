**Example 1: xx**

概览页

Input: 

```
tccli dsgc DescribeDSPAESDataAssetByComplianceId --cli-unfold-argument  \
    --DspaId abc \
    --ComplianceId 0
```

Output: 
```
{
    "Response": {
        "Stats": {
            "DataAssetType": 0,
            "SensitiveIndexCnt": 0,
            "TotalIndexCnt": 0,
            "SensitiveFieldCnt": 0,
            "TotalFieldCnt": 0,
            "SensitiveCategoryCnt": 0,
            "SensitiveLevel": [
                {
                    "LevelId": 0,
                    "LevelCnt": 0,
                    "LevelRiskName": "abc",
                    "LevelRiskScore": 0
                }
            ],
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

