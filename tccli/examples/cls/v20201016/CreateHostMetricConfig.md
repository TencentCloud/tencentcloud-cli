**Example 1: 创建主机指标采集配置**



Input: 

```
tccli cls CreateHostMetricConfig --cli-unfold-argument  \
    --TopicId 55fdd8a0-1a33-4ce3-8166-01f2361f0cdf \
    --Name host_metric_config_test \
    --MachineGroupIds c8bdead9-0170-4d69-ab08-5caa607b76d0 \
    --Interval 50000 \
    --HostMetricItems.0.Type cpu \
    --HostMetricItems.1.Type mem \
    --HostMetricItems.2.Type net \
    --HostMetricItems.3.Type disk \
    --HostMetricItems.4.Type system
```

Output: 
```
{
    "Response": {
        "ConfigId": "e542d884-f08b-4be9-b700-2a99d9aa1545",
        "RequestId": "2a1f4deb-c47a-46d4-bb7a-565a17e6aa38"
    }
}
```

