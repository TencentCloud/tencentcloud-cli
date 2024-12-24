**Example 1: 获取COS分类分级任务结果详情**



Input: 

```
tccli dsgc DescribeDSPACOSTaskResultDetail --cli-unfold-argument  \
    --DspaId dspa-890asdj2 \
    --TaskId 1 \
    --LevelId 10000 \
    --FileName file.txt \
    --Limit 10 \
    --ComplianceId 1 \
    --Offset 0 \
    --BucketResultId 1 \
    --BucketName bucket_1 \
    --CategoryId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "FileResultId": 1,
                "TaskId": 1,
                "ResultId": 1,
                "FileName": "file.txt",
                "ComplianceId": 1,
                "BucketName": "bucket_1",
                "RuleId": 10,
                "RuleName": "手机",
                "CategoryId": 1,
                "CategoryName": "个人基本信息",
                "CategoryFullPath": [
                    "个人基本信息"
                ],
                "LevelId": 2,
                "LevelName": "中",
                "LevelRiskScore": 5,
                "KMSEncrypted": false,
                "FileSize": 0,
                "FileType": "txt",
                "SensitiveDataCount": 1
            }
        ],
        "RequestId": "1f1765cf-c01a-4a93-95b2-99108f4aa04f"
    }
}
```

