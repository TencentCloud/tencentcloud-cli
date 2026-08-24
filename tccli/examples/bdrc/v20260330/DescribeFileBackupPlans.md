**Example 1: 查询备份计划列表**



Input: 

```
tccli bdrc DescribeFileBackupPlans --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "PlanSet": [
            {
                "AspPolicy": {
                    "AspId": "abp-7riwzmpp",
                    "AspName": "adminpolicy",
                    "AspState": "normal",
                    "CreateTime": "2026-06-10T21:15:45",
                    "IsActivated": true,
                    "IsPermanent": false,
                    "Policy": [
                        {
                            "Hour": [
                                0
                            ],
                            "IntervalDays": 1
                        }
                    ],
                    "RetentionDays": 0
                },
                "BackupCount": 0,
                "BackupPaths": [
                    "/tmp"
                ],
                "CreatedTime": "2026-06-10T21:16:12",
                "ExcludePatterns": [],
                "ExcludeSystemDirectories": true,
                "FlowControlSettings": [],
                "IncludeFileTypes": [],
                "LastExecuteTime": "2026-06-11T00:00:14",
                "LastTriggerError": "",
                "NextTriggerTime": "2026-06-12T00:00:00",
                "PlanId": "fbp-rbr9gp29",
                "PlanName": "未命名",
                "ResourceIds": [
                    "ins-852rp810"
                ],
                "Status": "normal",
                "VaultId": "vault-ivsapm9k"
            }
        ],
        "TotalCount": 8,
        "RequestId": "d9e76b63-23cb-431c-afc2-beb98e132c65"
    }
}
```

