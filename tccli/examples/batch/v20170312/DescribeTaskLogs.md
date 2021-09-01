**Example 1: 获取任务日志详情**



Input: 

```
tccli batch DescribeTaskLogs --cli-unfold-argument  \
    --JobId job-mawzp3ja \
    --TaskName task \
    --TaskInstanceIndexes 0 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskInstanceLogSet": [
            {
                "StdoutLog": "data:text/plain;charset=utf-8;base64,bWFpbgpbJ2RlbW8ucHknLCAnMycsICcvbW50L2lucHV0JywgJy9tbnQvb3V0cHV0JywgJzEnXWZsdXNoIHRvIC9tbnQvb3V0cHV0LzE1MzU3MjYwMDQuOTEKZmx1c2ggdG8gL21udC9vdXRwdXQvMTUzNTcyNjAwNi4zOQpmbHVzaCB0byAvbW50L291dHB1dC8xNTM1NzI2MDA3LjcK",
                "TaskInstanceIndex": 0,
                "StderrLog": "data:text/plain;charset=utf-8;base64,Zmx1c2ggdG8gL21udC9vdXRwdXQvMTUzNTcyNjAwNC45MQpmbHVzaCB0byAvbW50L291dHB1dC8xNTM1NzI2MDA2LjM5CmZsdXNoIHRvIC9tbnQvb3V0cHV0LzE1MzU3MjYwMDcuNwo=",
                "StdoutRedirectPath": "",
                "StderrRedirectPath": "",
                "StdoutRedirectFileName": "",
                "StderrRedirectFileName": ""
            }
        ],
        "RequestId": "3b1ba3bf-a315-42ec-9e8e-af8def768f8a"
    }
}
```

