**Example 1: 列出 Prometheus Agent**

查询 Prometheus Agent 列表

Input: 

```
tccli monitor DescribePrometheusAgents --cli-unfold-argument  \
    --InstanceId prom-m4fb9h34
```

Output: 
```
{
    "Response": {
        "AgentSet": [
            {
                "AgentId": "agent-hod16m34",
                "Name": "node-agent",
                "InstanceId": "prom-m4fb9h34",
                "HeartbeatTime": "2021-12-03T16:16:24+08:00",
                "Ipv4": "199.21.24.90",
                "LastError": "",
                "AgentVersion": "2.31.1-rig.1"
            }
        ],
        "RequestId": "e6a09531-0b40-41ab-a932-33061e9e1832",
        "TotalCount": 12
    }
}
```

