**Example 1: 获取运行时列表**

返回用户的运行时列表，运行时管理主页使用，包含沙箱、共享运行时及独立运行时环境，不包含已经删除的运行时

Input: 

```
tccli eis ListRuntimesMC --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Runtimes": [
            {
                "Status": 0,
                "AutoRenewal": true,
                "CpuLimit": 0.0,
                "DisplayName": "xx",
                "RunningInstanceCount": 2,
                "Zone": "xx",
                "Type": 2,
                "RuntimeType": 0,
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
            }
        ]
    }
}
```

