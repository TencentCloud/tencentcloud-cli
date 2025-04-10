**Example 1: DeleteClusterSnapshot 删除集群快照数据**



Input: 

```
tccli es DeleteClusterSnapshot --cli-unfold-argument  \
    --InstanceId es-al4radfu \
    --RepositoryName ES_AUTO_BACKUP \
    --SnapshotName es-al4radfu_20231120
```

Output: 
```
{
    "Response": {
        "InstanceId": "es-al4radfu",
        "RequestId": "xxx-xxxx"
    }
}
```

