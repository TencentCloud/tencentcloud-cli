**Example 1: 创建实例快照**

创建实例快照

Input: 

```
tccli lighthouse CreateInstanceSnapshot --cli-unfold-argument  \
    --InstanceId lhins-k31c771o \
    --SnapshotName snap_20200903
```

Output: 
```
{
    "Response": {
        "SnapshotId": "lhsnap-nv6aqcv6",
        "RequestId": "0580622c-03ef-4ae0-8192-016783412094"
    }
}
```

