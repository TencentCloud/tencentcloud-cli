**Example 1: 获取运行时列表**

返回用户的运行时列表，运行时管理主页使用，包含沙箱、共享运行时及独立运行时环境，不包含已经删除的运行时

Input: 

```
tccli eis ListRuntimesMC --cli-unfold-argument  \
    --RuntimeClass 0
```

Output: 
```
{
    "Response": {
        "Runtimes": [
            {
                "RuntimeId": 0,
                "Uin": "abc",
                "DisplayName": "abc",
                "Zone": "abc",
                "Type": 0,
                "Status": 0,
                "CreatedAt": 0,
                "UpdatedAt": 0,
                "WorkerSize": 0,
                "WorkerReplica": 0,
                "RunningInstanceCount": 0,
                "CpuUsed": 0,
                "CpuLimit": 0,
                "MemoryUsed": 0,
                "MemoryLimit": 0,
                "ExpiredAt": 0,
                "ChargeType": 0,
                "ResourceLimitType": 0,
                "AutoRenewal": true,
                "WorkerExtensions": [
                    {
                        "Type": 0,
                        "Size": 0,
                        "Replica": 0,
                        "Name": "abc",
                        "Status": 0,
                        "CreatedAt": 0,
                        "UpdatedAt": 0
                    }
                ],
                "RuntimeType": 0,
                "RuntimeClass": 0,
                "BandwidthOutUsed": 0,
                "BandwidthOutLimit": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

