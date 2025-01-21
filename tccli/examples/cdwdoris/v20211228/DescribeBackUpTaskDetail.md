**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeBackUpTaskDetail --cli-unfold-argument  \
    --InstanceId str \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "str",
        "BackupStatus": [
            {
                "Status": "str",
                "FinishedTime": "str",
                "BackupObjects": "str",
                "SnapshotName": "str",
                "TaskErrMsg": "str",
                "JobId": 0,
                "UnfinishedTasks": "str",
                "State": "str",
                "SnapshotFinishedTime": "str",
                "Timeout": 0,
                "UploadFinishedTime": "str",
                "Progress": "str",
                "CreateTime": "str",
                "DbName": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

