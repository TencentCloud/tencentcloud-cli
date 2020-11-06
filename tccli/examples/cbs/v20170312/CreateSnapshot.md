**Example 1: Creating a snapshot**



Input: 

```
tccli cbs CreateSnapshot --cli-unfold-argument  \
    --DiskId disk-lzrg2pwi \
    --SnapshotName snap_201711301015
```

Output: 
```
{
    "Response": {
        "SnapshotId": "snap-gybrif0z",
        "RequestId": "1bd35eca-0c9a-6e0b-938a-5a1f80511c19"
    }
}
```

