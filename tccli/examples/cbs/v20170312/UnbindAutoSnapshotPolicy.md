**Example 1: 解绑定期快照策略**

解绑定期快照策略

Input: 

```
tccli cbs UnbindAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-mrsrn243 \
    --DiskIds disk-dw0bbzws
```

Output: 
```
{
    "Response": {
        "RequestId": "52ba40b8-018b-d906-cad3-5a1fa6542fd6"
    }
}
```

