**Example 1: UpdateAutoSnapshotPolicy**

更新文件系统快照策略

Input: 

```
tccli cfs UpdateAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-12345 \
    --PolicyName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "AutoSnapshotPolicyId": "asp-12345"
    }
}
```

