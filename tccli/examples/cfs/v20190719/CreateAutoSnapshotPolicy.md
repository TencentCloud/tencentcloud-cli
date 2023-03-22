**Example 1: 创建文件系统快照策略**

创建文件系统快照策略

Input: 

```
tccli cfs CreateAutoSnapshotPolicy --cli-unfold-argument  \
    --DayOfWeek "1,2" \
    --Hour "2,3"
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

