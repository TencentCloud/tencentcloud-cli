**Example 1: 导入快照**

导入快照数据

Input: 

```
tccli tcaplusdb ImportSnapshots --cli-unfold-argument  \
    --ClusterId abc \
    --Snapshots.TableGroupId abc \
    --Snapshots.TableName abc \
    --Snapshots.SnapshotName abc \
    --Snapshots.SnapshotTime 2020-09-22 00:00:00 \
    --Snapshots.SnapshotDeadTime 2020-09-22 00:00:00 \
    --ImportSpecialKey abc \
    --KeyFile.FileName abc \
    --KeyFile.FileExtType abc \
    --KeyFile.FileContent abc \
    --KeyFile.FileSize 0 \
    --ImportOriginTable abc \
    --NewTableGroupId abc \
    --NewTableName abc
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "ApplicationId": "abc",
        "RequestId": "abc"
    }
}
```

