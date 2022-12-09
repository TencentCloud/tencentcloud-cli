**Example 1: 更新 Prometheus Agent 状态**



Input: 

```
tccli monitor UpdatePrometheusAgentStatus --cli-unfold-argument  \
    --InstanceId prom-abcd1234 \
    --AgentIds agent-abcd1234 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

