**Example 1: 查询备份列表**



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
                "AspInstanceId": "abp-adr398np",
                "BackupFileCount": 0,
                "BackupId": "fb-85u51cp0",
                "BackupName": "auto_ins-an553jqi_20260820_04",
                "BackupPaths": [
                    "/data"
                ],
                "BackupSize": 0,
                "BackupSizeFormatted": "0 B",
                "CreatedTime": "2026-08-20T04:00:06",
                "Deadline": "",
                "EndTime": "",
                "ExcludePatterns": [],
                "ExcludeSystemDirectories": true,
                "FailReason": "",
                "IncludeFileTypes": [],
                "IsPermanent": false,
                "JobId": "j-20260819200007-a7961c9b",
                "NonExistSourcePaths": [],
                "PlanId": "fbp-k6jm18un",
                "Progress": 0,
                "ResourceId": "ins-an553jqi",
                "ResourceType": "CVM_AGENT",
                "ScannedFileCount": 0,
                "ScannedSize": 0,
                "ScannedSizeFormatted": "0 B",
                "StartTime": "",
                "Status": 1,
                "VaultId": "vault-hrvkughn"
            }
        ],
        "TotalCount": 462,
        "RequestId": "81695377-1d73-44e0-a121-e5855b3b938b"
    }
}
```

