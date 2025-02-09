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
            "Install": "/bin/bash -c \"$(curl -fsSL https:/cos-url/install.sh)\"",
            "Restart": "systemctl restart prometheus-agent",
            "Stop": "systemctl stop prometheus-agent",
            "StatusCheck": "systemctl status prometheus-agent",
            "LogCheck": "journalctl -u prometheus-agent"
        },
        "RequestId": "as131asfjl23dsf342lxdsf"
    }
}
```

