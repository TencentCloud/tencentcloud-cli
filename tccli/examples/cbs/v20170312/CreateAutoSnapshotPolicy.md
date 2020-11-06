**Example 1: 创建定期快照策略**

创建一个定期快照策略，绑定该定期快照策略的云盘会在每周5的0点创建快照。

Input: 

```
tccli cbs CreateAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyName backup_data_friday \
    --Policy.0.DayOfWeek 4 \
    --Policy.0.Hour 0
```

Output: 
```
{
    "Response": {
        "AutoSnapshotPolicyId": "asp-1lebc9r3",
        "NextTriggerTime": "2018-08-08 16:00:00",
        "RequestId": "88d95732-c4e9-bd97-4a23-5a1f978d3b72"
    }
}
```

