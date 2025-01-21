**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeRestoreTaskDetail --cli-unfold-argument  \
    --InstanceId cdwdoris-xxx \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "RestoreStatus": [
            {
                "Status": "str",
                "FinishedTime": "str",
                "MetaPreparedTime": "str",
                "RestoreObjects": "str",
                "Timestamp": "str",
                "ReplicaAllocation": "str",
                "TaskErrMsg": "str",
                "JobId": 0,
                "CreateTime": "str",
                "State": "str",
                "SnapshotFinishedTime": "str",
                "Timeout": 0,
                "DownloadFinishedTime": "str",
                "UnfinishedTasks": "str",
                "Progress": "str",
                "Label": "str",
                "ReplicationNum": "str",
                "DbName": "str",
                "ReserveReplica": true,
                "ReserveDynamicPartitionEnable": true,
                "AllowLoad": true
            }
        ],
        "RequestId": "str",
        "ErrorMsg": "str"
    }
}
```

