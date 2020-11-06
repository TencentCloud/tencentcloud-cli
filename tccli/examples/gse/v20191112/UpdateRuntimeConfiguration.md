**Example 1: 更新服务器舰队配置**

更新服务器舰队配置

Input: 

```
tccli gse UpdateRuntimeConfiguration --cli-unfold-argument  \
    --FleetId fleet-pro4eunl-lmpa6tud \
    --RuntimeConfiguration.GameServerSessionActivationTimeoutSeconds 9 \
    --RuntimeConfiguration.MaxConcurrentGameServerSessionActivations 9 \
    --RuntimeConfiguration.ServerProcesses.0.ConcurrentExecutions 9 \
    --RuntimeConfiguration.ServerProcesses.0.LaunchPath /local/game/GameLiftLinuxServer \
    --RuntimeConfiguration.ServerProcesses.0.Parameters -cconf
```

Output: 
```
{
    "Response": {
        "RequestId": "90b59a79-9868-4145-8ff3-2053de2d785e",
        "RuntimeConfiguration": {
            "GameServerSessionActivationTimeoutSeconds": 9,
            "MaxConcurrentGameServerSessionActivations": 9,
            "ServerProcesses": [
                {
                    "ConcurrentExecutions": 9,
                    "LaunchPath": "/local/game/GameLiftLinuxServer",
                    "Parameters": "-c conf"
                }
            ]
        }
    }
}
```

