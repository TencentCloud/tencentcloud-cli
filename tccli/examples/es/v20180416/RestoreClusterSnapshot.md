**Example 1: RestoreClusterSnapshot 恢复快照数据到集群**



Input: 

```
tccli es RestoreClusterSnapshot --cli-unfold-argument  \
    --InstanceId es-qpzizjym \
    --Password abc \
    --RepositoryName ES_AUTO_BACKUP \
    --SnapshotName test1 \
    --Indices abc \
    --Partial true \
    --TargetInstanceId es-qpzizjym
```

Output: 
```
{
    "Response": {
        "InstanceId": "es-qpzizjym",
        "RequestId": "abc"
    }
}
```

