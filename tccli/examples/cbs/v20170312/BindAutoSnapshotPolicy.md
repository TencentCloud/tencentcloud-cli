**Example 1: 给单块盘绑定定期快照策略**

给单块盘绑定定期快照策略

Input: 

```
tccli cbs BindAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-mrsrn243 \
    --DiskIds disk-dw0bbzws
```

Output: 
```
{
    "Response": {
        "RequestId": "bda8bd1a-754d-d71b-8300-5a1fa45c237f"
    }
}
```

