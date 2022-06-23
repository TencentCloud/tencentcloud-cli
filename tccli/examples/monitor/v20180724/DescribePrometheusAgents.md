**Example 1: 列出 Prometheus Agent**



Input: 

```
tccli monitor DescribePrometheusAgents --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "AgentSet": [
            {
                "AgentId": "xx",
                "Name": "xx",
                "InstanceId": "xx",
                "HeartbeatTime": "xx",
                "Ipv4": "xx",
                "LastError": "xx",
                "AgentVersion": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalCount": 12
    }
}
```

