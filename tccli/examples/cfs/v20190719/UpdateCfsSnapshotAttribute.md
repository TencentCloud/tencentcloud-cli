**Example 1: 更新快照内容**



Input: 

```
tccli cfs UpdateCfsSnapshotAttribute --cli-unfold-argument  \
    --SnapshotId snapcfs-agabg \
    --SnapshotName defaultsnapshot \
    --AliveDays 1
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "SnapshotId": "snapcfs-agabg"
    }
}
```

