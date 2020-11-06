**Example 1: Sharing a snapshot with users**



Input: 

```
tccli cbs ModifySnapshotsSharePermission --cli-unfold-argument  \
    --AccountIds 123456789 \
    --Permission SHARE \
    --SnapshotIds snap-cgrmci8t snap-124p95lf
```

Output: 
```
{
    "RequestId": "4ab150b9-538d-48fb-8821-7fa185f1d07c"
}
```

