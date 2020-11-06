**Example 1: 查询云盘disk-dw0bbzws绑定的定期快照策略**



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
                "IsActivated": 1,
                "AutoSnapshotPolicyName": "sds",
                "IsPermanent": 0,
                "NextTriggerTime": "2017-12-03 00:00:00",
                "AutoSnapshotPolicyId": "asp-mrsrn243",
                "Policy": [
                    {
                        "DayOfWeek": [
                            0
                        ],
                        "Hour": [
                            0
                        ]
                    }
                ],
                "CreateTime": "2017-11-17 15:09:12",
                "RetentionDays": 7
            }
        ],
        "TotalCount": 1,
        "RequestId": "8612f14a-fd07-85b5-39f9-5a1fa51efa14"
    }
}
```

