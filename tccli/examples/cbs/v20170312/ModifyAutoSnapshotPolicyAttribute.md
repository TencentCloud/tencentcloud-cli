**Example 1: Modifying Scheduled Snapshot Policy Attributes**

The name of the scheduled snapshot policy to be modified is `data_disk_auto_snapshot`. `IsPermanent` is set to `TRUE`. Snapshots created by this scheduled snapshot policy are retained permanently.

Input: 

```
tccli cbs ModifyAutoSnapshotPolicyAttribute --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-nqu08k2l \
    --AutoSnapshotPolicyName data_disk_auto_snapshot \
    --IsPermanent TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "384c1fa8-6973-9623-b6bf-5a1fa9a7ad88"
    }
}
```

