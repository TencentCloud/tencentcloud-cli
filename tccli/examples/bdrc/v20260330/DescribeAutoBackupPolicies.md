**Example 1: 查询定期备份策略列表**



Input: 

```
tccli bdrc DescribeAutoBackupPolicies --cli-unfold-argument  \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "AutoBackupPolicySet": [
            {
                "AccountName": "",
                "AccountUin": "700002687914",
                "AdvancedRetentionPolicy": {},
                "AppId": 260202272,
                "AutoBackupPolicyId": "abp-fz96zo6z",
                "AutoBackupPolicyName": "[01.00_18.00]full_system_backup_strategy",
                "AutoBackupPolicyState": "NORMAL",
                "CreateTime": "2026-06-08T17:37:38+08:00",
                "InstanceIdSet": [
                    "ins-mpd1f3mq"
                ],
                "IsActivated": true,
                "IsPermanent": false,
                "NextTriggerTime": "2026-06-10T01:00:00+08:00",
                "Policy": [
                    {
                        "Hour": [
                            1
                        ],
                        "IntervalDays": 1
                    }
                ],
                "RetentionAmount": 3,
                "RetentionDays": 0,
                "RetentionMonths": 0,
                "StorageType": "COMMON",
                "SubAccountUin": "700002687914",
                "VaultId": ""
            }
        ],
        "TotalCount": 3,
        "RequestId": "a5fc934f-e73e-4c7c-9e1c-204898acc607"
    }
}
```

