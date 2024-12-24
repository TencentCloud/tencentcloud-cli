**Example 1: 获取COS分类分级数据资产详情**



Input: 

```
tccli dsgc DescribeDSPACOSDataAssetDetail --cli-unfold-argument  \
    --DspaId dspa-1f96daa1 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "BucketName": "bucekt_1",
                "FileName": "cds.txt",
                "RuleName": "通用",
                "SensitiveDataCount": 0,
                "CategoryName": "个人身份信息",
                "LevelRiskName": "系统-敏感",
                "KMSEncrypted": true,
                "FileType": ".txt",
                "FileSize": "10000",
                "LevelRiskScore": 1,
                "DataSourceId": "cos-d653df8923hjrhjc9",
                "RuleId": 100,
                "ResourceRegion": "ap-guangzhou",
                "CategoryId": 12,
                "LevelId": 8,
                "FileResultId": 0,
                "DataSourceName": "bucekt_1",
                "CategoryFullPath": "[\"个人基本信息\"]",
                "IdentifyType": 0,
                "CheckStatus": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

