**Example 1: 查看快照操作限制列表**



Input: 

```
tccli lighthouse DescribeSnapshotsDeniedActions --cli-unfold-argument  \
    --SnapshotIds lhsnap-nv6aqcv6
```

Output: 
```
{
    "Response": {
        "SnapshotDeniedActionSet": [
            {
                "SnapshotId": "lhsnap-nv6aqcv6",
                "DeniedActions": [
                    {
                        "Action": "RollbackInstanceSnapshot",
                        "Code": "UnsupportedOperation.DiskLatestOperationUnfinished",
                        "Message": "磁盘 `lhdisk-f71kc5bh` 正在进行 `回滚实例快照` 操作，不支持该操作"
                    },
                    {
                        "Action": "DeleteSnapshots",
                        "Code": "UnsupportedOperation.InvalidSnapshotState",
                        "Message": "快照 `lhsnap-nv6aqcv6` 处于 `回滚中` 状态中，不支持该操作"
                    }
                ]
            }
        ],
        "RequestId": "82069c10-0228-4ffa-a649-81b2b4e85513"
    }
}
```

