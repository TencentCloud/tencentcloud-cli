**Example 1: DescribeUserQuota**



Input: 

```
tccli goosefs DescribeUserQuota --cli-unfold-argument  \
    --FileSystemId x-c60-4lu862qo
```

Output: 
```
{
    "Response": {
        "QuotaList": [
            {
                "CreateTime": "2025-08-01T14:27:40+08:00",
                "ModifyTime": "2025-08-01T14:27:40+08:00",
                "QuotaFilesLimit": "100",
                "QuotaFilesUsed": "0",
                "QuotaFilesUsedPercent": "0%",
                "QuotaId": "quota_1754029660656",
                "QuotaObjectName": "40001",
                "QuotaSizeLimit": "10G",
                "QuotaSizeUsed": "0K",
                "QuotaSizeUsedPercent": "0%",
                "QuotaType": "UID",
                "Status": "active"
            },
            {
                "CreateTime": "2025-08-01T14:32:25+08:00",
                "ModifyTime": "2025-08-01T14:32:25+08:00",
                "QuotaFilesLimit": "1000000",
                "QuotaFilesUsed": "0",
                "QuotaFilesUsedPercent": "0%",
                "QuotaId": "quota_1754029945731",
                "QuotaObjectName": "40002",
                "QuotaSizeLimit": "100G",
                "QuotaSizeUsed": "0K",
                "QuotaSizeUsedPercent": "0%",
                "QuotaType": "UID",
                "Status": "active"
            }
        ],
        "RequestId": "2465b710-dbee-4254-86d5-9ef9972ed550"
    }
}
```

