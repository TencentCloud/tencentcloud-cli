**Example 1: 下载日志信息**



Input: 

```
tccli wedata DownloadLogByLine --cli-unfold-argument  \
    --TaskId 123 \
    --CurRunDate 123 \
    --DetailId 123 \
    --StartLine 0 \
    --LineCount 0 \
    --FilePath 123 \
    --ProjectId 123 \
    --RecordId 123
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 0,
            "Content": [
                "123"
            ],
            "Over": true,
            "InstanceState": "123",
            "InstanceId": "123",
            "TaskId": "123",
            "WorkerType": 0
        },
        "RequestId": "123"
    }
}
```

