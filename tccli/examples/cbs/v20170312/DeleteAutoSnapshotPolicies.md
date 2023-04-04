**Example 1: 批量删除定期快照策略**

删除指定定期快照策略：asp-mrsrn243、asp-3lpl7ev3

Input: 

```
tccli cbs DeleteAutoSnapshotPolicies --cli-unfold-argument  \
    --AutoSnapshotPolicyIds asp-mrsrn243 asp-3lpl7ev3
```

Output: 
```
{
    "Response": {
        "RequestId": "60874256-0230-6c3b-371d-5a1fa64e6b8c"
    }
}
```

