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
                "DisplayName": "xx",
                "Zone": "xx",
                "Uin": "xx",
                "WorkerReplica": 0,
                "UpdatedAt": 1624354153,
                "Type": 2,
                "RuntimeId": 123,
                "CreatedAt": 1624354153,
                "WorkerSize": 2,
                "RunningInstanceCount": 2,
                "CpuLimit": 2,
                "CpuUsed": 0.055,
                "MemoryLimit": 4096,
                "MemoryUsed": 703.605
            }
        ]
    }
}
```

