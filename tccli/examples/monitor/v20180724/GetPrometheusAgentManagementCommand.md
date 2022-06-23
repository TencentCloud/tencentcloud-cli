**Example 1: 获取 Prometheus Agent 管理相关的命令行**



Input: 

```
tccli monitor GetPrometheusAgentManagementCommand --cli-unfold-argument  \
    --InstanceId prom-23kdafdf \
    --AgentId agent-23kdafdf
```

Output: 
```
{
    "Response": {
        "Command": {
            "Install": "xx",
            "Restart": "xx",
            "Stop": "xx",
            "StatusCheck": "xx",
            "LogCheck": "xx"
        },
        "RequestId": "as131asfjl23dsf342lxdsf"
    }
}
```

