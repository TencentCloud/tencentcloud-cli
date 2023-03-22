**Example 1: 绑定文件系统快照策略**

绑定文件系统快照策略

Input: 

```
tccli cfs BindAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-12345 \
    --FileSystemIds cfs-12345
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

