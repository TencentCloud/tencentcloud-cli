**Example 1: 查询备份日志列表**

查询备份日志列表

Input: 

```
tccli csip DescribeDspmBackupLogList --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Sort desc \
    --Field ip \
    --StartTime 0 \
    --EndTime 0 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "Id": 0,
                "IndexStartTime": 0,
                "IndexEndTime": 0,
                "BackupSize": 0,
                "Status": 0,
                "RestoreProcessRemindTime": 0,
                "RestoreRemindTime": 0
            }
        ],
        "RequestId": "24adbdda-a605-4501-9e8c-3f0894936a62"
    }
}
```

