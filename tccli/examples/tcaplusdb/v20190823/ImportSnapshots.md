**Example 1: 导入快照**

导入快照数据

Input: 

```
tccli tcaplusdb ImportSnapshots --cli-unfold-argument  \
    --ClusterId xx \
    --Snapshots.SnapshotName xx \
    --Snapshots.TableGroupId xx \
    --Snapshots.SnapshotTime 2020-09-22 00:00:00 \
    --Snapshots.TableName xx \
    --Snapshots.SnapshotDeadTime 2020-09-22 00:00:00 \
    --NewTableGroupId xx \
    --ImportOriginTable xx \
    --KeyFile.FileExtType xx \
    --KeyFile.FileSize 0 \
    --KeyFile.FileContent xx \
    --KeyFile.FileName xx \
    --ImportSpecialKey xx \
    --NewTableName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

