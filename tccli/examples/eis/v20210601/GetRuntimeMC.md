**Example 1: 获取运行时详情**



Input: 

```
tccli eis GetRuntimeMC --cli-unfold-argument  \
    --RuntimeId 12 \
    --Zone xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Runtime": {
            "Status": 1,
            "DisplayName": "xx",
            "Zone": "xx",
            "Uin": "xx",
            "WorkerReplica": 0,
            "UpdatedAt": 1624354153,
            "Type": 2,
            "RuntimeId": 123,
            "CreatedAt": 1624354153,
            "WorkerSize": 2,
            "RunningInstanceCount": 3
        }
    }
}
```

