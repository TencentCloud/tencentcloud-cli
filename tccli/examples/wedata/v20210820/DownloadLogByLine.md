**Example 1: 下载日志信息**



Input: 

```
tccli wedata DownloadLogByLine --cli-unfold-argument  \
    --TaskId 1 \
    --CurRunDate 1 \
    --DetailId 1 \
    --StartLine 0 \
    --LineCount 0 \
    --FilePath 1 \
    --ProjectId 1 \
    --RecordId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 0,
            "Content": [
                "1"
            ],
            "Over": true,
            "InstanceState": "1",
            "InstanceId": "1",
            "TaskId": "1",
            "WorkerType": 0
        },
        "RequestId": "1"
    }
}
```

