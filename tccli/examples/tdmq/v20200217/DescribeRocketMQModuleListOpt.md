**Example 1: test**



Input: 

```
tccli tdmq DescribeRocketMQModuleListOpt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "ConfigModules": [
            {
                "ModuleName": "bk_env",
                "ComponentName": "BOOKIE",
                "ConfigName": "bkenv.sh",
                "IsShell": true
            },
            {
                "ModuleName": "bookie",
                "ComponentName": "BOOKIE",
                "ConfigName": "bookkeeper.conf",
                "IsShell": false
            },
            {
                "ModuleName": "tracing_agent",
                "ComponentName": "BROKER",
                "ConfigName": "agent.config",
                "IsShell": false
            },
            {
                "ModuleName": "broker",
                "ComponentName": "BROKER",
                "ConfigName": "broker.conf",
                "IsShell": false
            },
            {
                "ModuleName": "client",
                "ComponentName": "BROKER",
                "ConfigName": "client.conf",
                "IsShell": false
            },
            {
                "ModuleName": "monitor_sh",
                "ComponentName": "BROKER",
                "ConfigName": "monitor.sh",
                "IsShell": true
            },
            {
                "ModuleName": "pulsar_env",
                "ComponentName": "BROKER",
                "ConfigName": "pulsar_env.sh",
                "IsShell": true
            },
            {
                "ModuleName": "token",
                "ComponentName": "BROKER",
                "ConfigName": "tdmqadmin-secret.key",
                "IsShell": true
            },
            {
                "ModuleName": "zookeeper",
                "ComponentName": "ZOOKEEPER_BOOKIE",
                "ConfigName": "zookeeper.conf",
                "IsShell": false
            },
            {
                "ModuleName": "zookeeper",
                "ComponentName": "ZOOKEEPER_BROKER",
                "ConfigName": "zookeeper.conf",
                "IsShell": false
            }
        ]
    }
}
```

