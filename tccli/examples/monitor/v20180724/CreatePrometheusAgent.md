**Example 1: 创建 Prometheus Agent**



Input: 

```
tccli monitor CreatePrometheusAgent --cli-unfold-argument  \
    --InstanceId prom-sd234234 \
    --Name example
```

Output: 
```
{
    "Response": {
        "AgentId": "agent-abcd",
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

