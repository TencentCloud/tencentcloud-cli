**Example 1: 示例1**

导出工作流

Input: 

```
tccli wedata ExportWorkflowZip --cli-unfold-argument  \
    --ProjectId 1460726726769418240 \
    --WorkflowIds 25287aef-7226-11ed-8346-e43d1ad5f5f0 7bf9d403-7fb5-11ed-8346-e43d1ad5f5f0
```

Output: 
```
{
    "Response": {
        "Data": {
            "BucketName": "wedata-fusion-dev-1257305158",
            "BucketRegion": "ap-nanjing",
            "FileExpireTime": 1688807018,
            "FileMappings": [
                {
                    "AbsoluteTargetFilePath": "/datastudio/tmp/export/1460726726769418240/1460726726769418240_workflows_20230623170338092.zip",
                    "OriginFileName": "1460726726769418240_workflows_20230623170338092.zip",
                    "TargetFileName": "1460726726769418240_workflows_20230623170338092.zip"
                }
            ],
            "SecretId": "AKIDm8idO32-h8JB0VOabcd",
            "SecretKey": "SIcPS0FKz9oXOXY2abcd",
            "ShareStorageEndPoint": "service.cos.myqcloud.com",
            "ShareStorageType": "COS",
            "Token": "35A7Jdz9uwbijSzVBYYZKcgpOFn1yBDad4a26ba4dc36c23ffcb436b79fd48e01G_cfFo-D8aDzgnLMh2krQNeHbxeDNgUoaqlEAyrofYT63cxSB2W5GDk9H9wir68aBluiN",
            "TokenCreateTime": 1687511018,
            "TokenExpiredTime": 1687518218
        },
        "RequestId": "679ac0d4-9587-42be-895b-de933aa775e7"
    }
}
```

