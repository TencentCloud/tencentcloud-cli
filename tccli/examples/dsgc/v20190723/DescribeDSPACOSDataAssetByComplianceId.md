**Example 1: 获取COS单个模板下的敏感数据资产**

分类分级的

Input: 

```
tccli dsgc DescribeDSPACOSDataAssetByComplianceId --cli-unfold-argument  \
    --DspaId dspa-00001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Stats": {
            "DataAssetType": 0,
            "TotalBucketCnt": 0,
            "TotalObjectCnt": 0,
            "SensitiveCategoryCnt": 0,
            "SensitiveDataCnt": 0,
            "SensitiveLevel": [
                {
                    "LevelId": 0,
                    "LevelCnt": 0,
                    "LevelRiskName": "abc",
                    "LevelRiskScore": 0
                }
            ],
            "SensitiveBucketCnt": 0,
            "SensitiveObjectCnt": 0,
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

