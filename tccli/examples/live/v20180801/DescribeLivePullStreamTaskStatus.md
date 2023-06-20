**Example 1: 请求示例**



Input: 

```
tccli live DescribeLivePullStreamTaskStatus --cli-unfold-argument  \
    --TaskId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "57ff5d4c-f864-41bb-93d8-17d215d3359e",
        "TaskStatusInfo": {
            "FileUrl": "",
            "LoopedTimes": -1,
            "OffsetTime": 0,
            "ReportTime": "",
            "FileDuration": 0,
            "NextFileUrl": "",
            "RunStatus": "inactive"
        }
    }
}
```

