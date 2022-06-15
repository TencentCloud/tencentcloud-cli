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
            "Status": 1,
            "AutoRenewal": true,
            "CpuLimit": 0.0,
            "DisplayName": "xx",
            "RunningInstanceCount": 3,
            "Zone": "xx",
            "Type": 2,
            "ExpiredAt": 0,
            "WorkerReplica": 0,
            "MemoryLimit": 0.0,
            "CpuUsed": 0.055,
            "ChargeType": 0,
            "UpdatedAt": 1624354153,
            "ResourceLimitType": 0,
            "RuntimeId": 123,
            "Uin": "xx",
            "MemoryUsed": 703.605,
            "CreatedAt": 1624354153,
            "WorkerSize": 2
        },
        "RequestId": "xx"
    }
}
```

