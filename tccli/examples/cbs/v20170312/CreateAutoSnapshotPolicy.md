**Example 1: Creating a Scheduled Snapshot Policy**

Creates a scheduled snapshot policy. The cloud disk this scheduled snapshot policy is bound to will create a snapshot at 00:00 every Friday.

Input: 

```
tccli cbs CreateAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyName backup_data_friday\
    --Policy.0.DayOfWeek 4\
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

