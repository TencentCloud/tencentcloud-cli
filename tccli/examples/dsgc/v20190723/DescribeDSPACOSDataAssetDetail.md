**Example 1: 获取COS分类分级数据资产详情**



Input: 

```
tccli dsgc DescribeDSPACOSDataAssetDetail --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Details": [
            {
                "BucketName": "bucket-xxxx",
                "FileName": "test.txt",
                "RuleName": "住址",
                "CategoryName": "个人基本信息",
                "LevelRiskName": "中",
                "KMSEncrypted": true,
                "FileType": "text",
                "FileSize": "32B"
            }
        ],
        "RequestId": "xx"
    }
}
```

