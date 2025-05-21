**Example 1: 查询Fileset**

查询Fileset

Input: 

```
tccli goosefs DescribeFilesets --cli-unfold-argument  \
    --FileSystemId x-c60-gq019g3k
```

Output: 
```
{
    "Response": {
        "FilesetList": [
            {
                "AuditState": "disable",
                "CreateTime": "2025-04-22T20:55:05+08:00",
                "FsetDir": "/fset/fset_test_001/",
                "FsetId": "fset_1745468035223",
                "FsetName": "fset_test_001",
                "ModifyTime": "2025-04-27T16:17:23+08:00",
                "QuotaFilesLimit": "1024",
                "QuotaFilesUsed": "2",
                "QuotaFilesUsedPercent": "0.20%",
                "QuotaSizeLimit": "1024G",
                "QuotaSizeUsed": "35651584K",
                "QuotaSizeUsedPercent": "3.32%",
                "Status": "active"
            },
            {
                "AuditState": "disable",
                "CreateTime": "2025-04-22T20:55:12+08:00",
                "FsetDir": "/fset/fset_test_002/",
                "FsetId": "fset_1745468035263",
                "FsetName": "fset_test_002",
                "ModifyTime": "2025-04-27T16:17:35+08:00",
                "QuotaFilesLimit": "1024",
                "QuotaFilesUsed": "2",
                "QuotaFilesUsedPercent": "0.20%",
                "QuotaSizeLimit": "1024G",
                "QuotaSizeUsed": "20971520K",
                "QuotaSizeUsedPercent": "1.95%",
                "Status": "active"
            },
            {
                "AuditState": "disable",
                "CreateTime": "2025-04-22T20:55:13+08:00",
                "FsetDir": "/fset/fset_test_003/",
                "FsetId": "fset_1745468035273",
                "FsetName": "fset_test_003",
                "ModifyTime": "2025-04-27T16:17:40+08:00",
                "QuotaFilesLimit": "1024",
                "QuotaFilesUsed": "2",
                "QuotaFilesUsedPercent": "0.20%",
                "QuotaSizeLimit": "1024G",
                "QuotaSizeUsed": "31457280K",
                "QuotaSizeUsedPercent": "2.93%",
                "Status": "active"
            },
            {
                "AuditState": "disable",
                "CreateTime": "2025-04-22T20:55:21+08:00",
                "FsetDir": "/fset/fset_test_004/",
                "FsetId": "fset_1745468035284",
                "FsetName": "fset_test_004",
                "ModifyTime": "2025-04-27T16:17:46+08:00",
                "QuotaFilesLimit": "1024",
                "QuotaFilesUsed": "1",
                "QuotaFilesUsedPercent": "0.10%",
                "QuotaSizeLimit": "1024G",
                "QuotaSizeUsed": "0K",
                "QuotaSizeUsedPercent": "0.00%",
                "Status": "active"
            },
            {
                "AuditState": "disable",
                "CreateTime": "2025-04-22T20:55:22+08:00",
                "FsetDir": "/fset/fset_test_005/",
                "FsetId": "fset_1745468035294",
                "FsetName": "fset_test_005",
                "ModifyTime": "2025-04-27T16:17:53+08:00",
                "QuotaFilesLimit": "1024",
                "QuotaFilesUsed": "1",
                "QuotaFilesUsedPercent": "0.10%",
                "QuotaSizeLimit": "1024G",
                "QuotaSizeUsed": "0K",
                "QuotaSizeUsedPercent": "0.00%",
                "Status": "active"
            }
        ],
        "RequestId": "2ab92d6c-dd47-429a-8b31-0ec56c574a2b"
    }
}
```

