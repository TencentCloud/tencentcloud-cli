**Example 1: 导入快照**

导入快照数据

Input: 

```
tccli tcaplusdb ImportSnapshots --cli-unfold-argument  \
    --ClusterId 1837232 \
    --Snapshots.TableGroupId 1 \
    --Snapshots.TableName testname \
    --Snapshots.SnapshotName snapshotname \
    --Snapshots.SnapshotTime 2020-09-22 00:00:00 \
    --Snapshots.SnapshotDeadTime 2020-09-22 00:00:00 \
    --ImportSpecialKey spkey \
    --KeyFile.FileName filename \
    --KeyFile.FileExtType txt \
    --KeyFile.FileContent content \
    --KeyFile.FileSize 12130 \
    --ImportOriginTable origintable \
    --NewTableGroupId newtable \
    --NewTableName newname
```

Output: 
```
{
    "Response": {
        "TaskId": "35452",
        "ApplicationId": "134425",
        "RequestId": "232523-121452"
    }
}
```

