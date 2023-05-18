**Example 1: 查询备份点列表**

查询备份点列表

Input: 

```
tccli cbs DescribeDiskBackups --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DiskBackupSet": [
            {
                "DiskBackupName": "11111",
                "Encrypt": false,
                "Percent": 100,
                "DiskBackupId": "dbp-xxxxxxxx",
                "DiskSize": 100,
                "DiskBackupState": "NORMAL",
                "DiskUsage": "DATA_DISK",
                "CreateTime": "2022-04-02T17:44:55+00:00",
                "DiskId": "disk-xxxxxxxx"
            }
        ],
        "RequestId": "6cd062f5-aa65-4477-a253-1ab41ab963fd"
    }
}
```

