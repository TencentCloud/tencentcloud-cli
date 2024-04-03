**Example 1: 启用自动快照策略**

启用自动快照策略

Input: 

```
tccli cbs ModifyAutoSnapshotPolicyAttribute --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-01928374 \
    --IsActivated true
```

Output: 
```
{
    "Response": {
        "RequestId": "88a4815c-4a09-4948-b0c9-fa6fdefe8e4a"
    }
}
```

**Example 2: 修改定期快照策略属性**

修改该定期快照策略的名称为data_disk_auto_snapshot，且将IsPermanent置为TRUE，通过该定期快照策略创建的快照为永久保留的快照。

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

