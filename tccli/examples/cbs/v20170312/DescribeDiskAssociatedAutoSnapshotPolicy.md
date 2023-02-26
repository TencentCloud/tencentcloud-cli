**Example 1: 查询云盘disk-dw0bbzws绑定的定期快照策略**

通过云硬盘ID查询云硬盘绑定的定期快照策略

Input: 

```
tccli cbs DescribeDiskAssociatedAutoSnapshotPolicy --cli-unfold-argument  \
    --DiskId disk-dw0bbzws
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
                "NextTriggerTime": "2023-02-24 23:00:00",
                "AutoSnapshotPolicyName": "Orch-data-1h-3d",
                "AutoSnapshotPolicyId": "asp-3drodm1k",
                "CopyFromAccountUin": null,
                "InstanceIdSet": [],
                "RetentionAmount": 0,
                "RetentionDays": 3,
                "Policy": [
                    {
                        "DayOfWeek": [
                            0,
                            1,
                            2,
                            3,
                            4,
                            5,
                            6
                        ],
                        "Hour": [
                            0,
                            1,
                            2,
                            3,
                            4,
                            5,
                            6,
                            7,
                            8,
                            9,
                            10,
                            11,
                            12,
                            13,
                            14,
                            15,
                            16,
                            17,
                            18,
                            19,
                            20,
                            21,
                            22,
                            23
                        ]
                    }
                ],
                "RetentionMonths": 0,
                "CreateTime": "2023-02-15 16:56:04",
                "CopyToAccountUin": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "a9f6fd41-242f-4053-89c2-73ac5465ed9c"
    }
}
```

