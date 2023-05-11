**Example 1: 将快照共享给用户**

将指定快照共享给另一个用户

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
    "Response": {
        "RequestId": "4ab150b9-538d-48fb-8821-7fa185f1d07c"
    }
}
```

