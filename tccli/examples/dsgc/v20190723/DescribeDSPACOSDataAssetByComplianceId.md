**Example 1: 获取COS单个模板下的敏感数据资产**

分类分级的

Input: 

```
tccli dsgc DescribeDSPACOSDataAssetByComplianceId --cli-unfold-argument  \
    --DspaId dspa-3n34nzca \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Stats": {
            "DataAssetType": 1,
            "TotalBucketCnt": 10,
            "TotalObjectCnt": 10,
            "SensitiveCategoryCnt": 5,
            "SensitiveDataCnt": 5,
            "SensitiveLevel": [
                {
                    "LevelId": 1,
                    "LevelCnt": 5,
                    "LevelRiskName": "高敏感",
                    "LevelRiskScore": 10
                }
            ],
            "SensitiveBucketCnt": 1,
            "SensitiveObjectCnt": 1,
            "CategoryDistributed": [
                {
                    "CategoryId": 1,
                    "CategoryName": "联系方式",
                    "Count": 1,
                    "CategoryFullPath": "个人基本信息/联系方式"
                }
            ]
        },
        "RequestId": "5af5a48c-6eb7-4d81-8df6-6d0e316a32ef"
    }
}
```

