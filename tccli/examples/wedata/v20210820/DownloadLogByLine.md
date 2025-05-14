**Example 1: 下载日志信息**



Input: 

```
tccli wedata DownloadLogByLine --cli-unfold-argument  \
    --TaskId abc \
    --CurRunDate abc \
    --DetailId abc \
    --StartLine 0 \
    --LineCount 0 \
    --FilePath abc \
    --ProjectId abc \
    --RecordId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 0,
            "Content": [
                "abc"
            ],
            "Over": true,
            "InstanceState": "abc",
            "InstanceId": "abc",
            "TaskId": "abc",
            "WorkerType": 0
        },
        "RequestId": "abc"
    }
}
```

