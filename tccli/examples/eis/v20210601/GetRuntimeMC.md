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
        "Runtime": {
            "DisplayName": "xx",
            "Zone": "xx",
            "MemoryUsed": 703.605,
            "Status": 1,
            "ResourceLimitType": 0,
            "Type": 2,
            "UpdatedAt": 1624354153,
            "RuntimeId": 123,
            "CpuLimit": 0.0,
            "CreatedAt": 1624354153,
            "WorkerSize": 2,
            "RuntimeClass": 0,
            "WorkerReplica": 0,
            "CpuUsed": 0.055,
            "RunningInstanceCount": 3,
            "ExpiredAt": 0,
            "Uin": "xx",
            "MemoryLimit": 0.0,
            "ChargeType": 0,
            "AutoRenewal": true,
            "RuntimeType": 0
        },
        "RequestId": "xx"
    }
}
```

