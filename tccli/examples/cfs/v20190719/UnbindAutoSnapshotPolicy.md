**Example 1: 解绑文件系统**



Input: 

```
tccli cfs UnbindAutoSnapshotPolicy --cli-unfold-argument  \
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

