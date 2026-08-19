**Example 1: 查看用户客户端运行模式配置**

查看用户客户端运行模式配置

Input: 

```
tccli csip DescribeAgentRunMode --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AdvanceModeQuuids": [
            "18d5ca9e-6880-43de-a4c5-d6e62fc6bb7b"
        ],
        "AdvancePolicy": {
            "Cpu": 30,
            "Memory": 300,
            "NetworkPps": 0
        },
        "BasicPolicy": {
            "Cpu": 0,
            "Memory": 200,
            "NetworkPps": 0
        },
        "CustomModeQuuids": [
            "0e595552-e57e-450d-989c-16e4d4e0a464"
        ],
        "CustomPolicy": {
            "Cpu": 30,
            "Memory": 0,
            "NetworkPps": 100000
        },
        "EnhanceLogMode": 1,
        "MalwarePocMode": 0,
        "ReportSourcePort": 0,
        "RequestId": "1a4d4ed6-bd5d-4990-9190-e0c3bb1997ba"
    }
}
```

