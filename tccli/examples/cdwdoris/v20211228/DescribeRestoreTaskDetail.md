**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeRestoreTaskDetail --cli-unfold-argument  \
    --InstanceId xx \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "RestoreStatus": [
            {
                "Status": "xx",
                "FinishedTime": "xx",
                "MetaPreparedTime": "xx",
                "RestoreObjects": "xx",
                "Timestamp": "xx",
                "ReplicaAllocation": "xx",
                "TaskErrMsg": "xx",
                "JobId": 0,
                "CreateTime": "xx",
                "State": "xx",
                "SnapshotFinishedTime": "xx",
                "Timeout": 0,
                "DownloadFinishedTime": "xx",
                "UnfinishedTasks": "xx",
                "Progress": "xx",
                "Label": "xx",
                "ReplicationNum": "xx",
                "DbName": "xx",
                "AllowLoad": true
            }
        ],
        "RequestId": "xx",
        "ErrorMsg": "xx"
    }
}
```

