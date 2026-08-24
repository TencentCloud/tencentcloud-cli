**Example 1: 查询备份列表详情**



Input: 

```
tccli bdrc DescribeFileBackups --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "BackupSet": [
            {
                "AspInstanceId": "",
                "BackupFileCount": 1351200,
                "BackupId": "fb-m9nvo7l4",
                "BackupName": "",
                "BackupPaths": [
                    "/data"
                ],
                "BackupSize": 40205298693,
                "BackupSizeFormatted": "37.44 GiB",
                "CreatedTime": "2026-04-01T15:00:34",
                "EndTime": "",
                "ExcludePatterns": null,
                "ExcludeSystemDirectories": true,
                "IncludeFileTypes": null,
                "JobId": "j-20260401070034-a018b0d8",
                "PlanId": null,
                "Progress": 34.14,
                "ResourceId": "ins-7630gzfm",
                "ScannedFileCount": 4000000,
                "ScannedSize": 117760571686,
                "ScannedSizeFormatted": "109.67 GiB",
                "StartTime": "2026-04-01T15:01:44",
                "Status": 1
            }
        ],
        "RequestId": "c7ffb5b2-1000-400c-806a-ce2bd1ae86c8",
        "TotalCount": 28
    }
}
```

