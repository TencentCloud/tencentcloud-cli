**Example 1: 获取COS分类分级任务结果详情**



Input: 

```
tccli dsgc DescribeDSPACOSTaskResultDetail --cli-unfold-argument  \
    --DspaId dspa-001 \
    --TaskId 0 \
    --LevelId 10000 \
    --FileName test.txt \
    --Limit 0 \
    --ComplianceId 0 \
    --Offset 0 \
    --BucketResultId 1 \
    --BucketName bucket_1 \
    --CategoryId 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "CategoryName": "身份证",
                "RuleId": 0,
                "LevelName": "高",
                "FileType": ".csv",
                "SensitiveDataCount": 0,
                "LevelId": 10000,
                "FileName": "test.txt",
                "LevelRiskScore": 0,
                "BucketName": "bucket_01",
                "TaskId": 0,
                "RuleName": "rule_01",
                "KMSEncrypted": true,
                "CategoryId": 0,
                "FileSize": 0
            }
        ],
        "RequestId": "request_001"
    }
}
```

