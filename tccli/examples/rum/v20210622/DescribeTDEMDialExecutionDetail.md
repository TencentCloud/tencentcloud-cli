**Example 1: 查询拨测批次详情**

按应用、任务、批次和时间窗查询这一批探测的连通性与路由追踪。

Input: 

```
tccli rum DescribeTDEMDialExecutionDetail --cli-unfold-argument  \
    --AppId 5 \
    --StartTime 1790092800000 \
    --EndTime 1790784000000 \
    --TaskId 1 \
    --TaskSessionId selftest-no-exec
```

Output: 
```
{
    "Response": {
        "AppVersion": "",
        "AvgDuration": 0,
        "Device": "",
        "NetType": "",
        "Operator": "",
        "Platform": "",
        "Probes": [],
        "Region": "",
        "SessionId": "",
        "StartTime": 0,
        "Success": false,
        "TargetIps": [],
        "TaskId": "1",
        "TaskName": "capi-selftest-0930-mod",
        "TaskSessionId": "selftest-no-exec",
        "RequestId": "fa3f3918-e88d-4327-b1fb-0818de977b79"
    }
}
```

