**Example 1: 查询状态为NORMAL的定期快照策略**

查询状态为NORMAL的定期快照策略

Input: 

```
tccli cbs DescribeAutoSnapshotPolicies --cli-unfold-argument  \
    --Filters.0.Name auto-snapshot-policy-state \
    --Filters.0.Values NORMAL
```

Output: 
```
{
    "Response": {
        "AutoSnapshotPolicySet": [
            {
                "DiskIdSet": [],
                "IsActivated": true,
                "AdvancedRetentionPolicy": null,
                "IsCopyToRemote": 0,
                "IsPermanent": false,
                "AutoSnapshotPolicyState": "NORMAL",
                "Tags": [],
                "NextTriggerTime": "2023-03-03 07:00:00",
                "AutoSnapshotPolicyName": "default-policy",
                "AutoSnapshotPolicyId": "asp-3stvwfxx",
                "CopyFromAccountUin": null,
                "InstanceIdSet": [],
                "RetentionAmount": 0,
                "RetentionDays": 15,
                "Policy": [
                    {
                        "DayOfWeek": [
                            6,
                            5
                        ],
                        "Hour": [
                            7
                        ]
                    }
                ],
                "RetentionMonths": 0,
                "CreateTime": "2022-05-16 14:00:48",
                "CopyToAccountUin": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "9c112e22-96c6-4300-831e-5d52c8d361fc"
    }
}
```

