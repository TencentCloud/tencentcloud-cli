**Example 1: 创建快照**

用户创建快照

Input: 

```
tccli cbs CreateSnapshot --cli-unfold-argument  \
    --SnapshotName snap_201711301015 \
    --Deadline 2022-01-08T09:47:55+00:00 \
    --DiskId disk-lzrg2pwi
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

