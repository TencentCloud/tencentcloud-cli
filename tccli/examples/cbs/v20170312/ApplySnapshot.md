**Example 1: 回滚快照**

回滚云盘某个快照节点

Input: 

```
tccli cbs ApplySnapshot --cli-unfold-argument  \
    --DiskId disk-lzrg2pwi \
    --SnapshotId snap-gybrif0z
```

Output: 
```
{
    "Response": {
        "RequestId": "cc96242e-566c-ae6a-b74a-5a1f823683b2"
    }
}
```

