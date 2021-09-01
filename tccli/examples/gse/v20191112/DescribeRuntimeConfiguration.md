**Example 1: 获取服务器舰队运行配置**

获取服务器舰队运行配置

Input: 

```
tccli gse DescribeRuntimeConfiguration --cli-unfold-argument  \
    --FleetId fleet-qp3g3fn6-p6l46gnu
```

Output: 
```
{
    "Response": {
        "RequestId": "s1582189364373611676",
        "RuntimeConfiguration": {
            "GameServerSessionActivationTimeoutSeconds": 600,
            "MaxConcurrentGameServerSessionActivations": 0,
            "ServerProcesses": [
                {
                    "ConcurrentExecutions": 10,
                    "LaunchPath": "/local/game/GameLiftLinuxServer",
                    "Parameters": ""
                }
            ]
        }
    }
}
```

