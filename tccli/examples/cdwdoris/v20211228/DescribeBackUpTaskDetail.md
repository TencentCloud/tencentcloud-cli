**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeBackUpTaskDetail --cli-unfold-argument  \
    --InstanceId xx \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "xx",
        "BackupStatus": [
            {
                "Status": "xx",
                "FinishedTime": "xx",
                "BackupObjects": "xx",
                "SnapshotName": "xx",
                "TaskErrMsg": "xx",
                "JobId": 0,
                "UnfinishedTasks": "xx",
                "State": "xx",
                "SnapshotFinishedTime": "xx",
                "Timeout": 0,
                "UploadFinishedTime": "xx",
                "Progress": "xx",
                "CreateTime": "xx",
                "DbName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

