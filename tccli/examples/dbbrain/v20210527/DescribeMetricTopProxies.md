**Example 1: DescribeMetricTopProxies test case**

获取redis proxy 指标

Input: 

```
tccli dbbrain DescribeMetricTopProxies --cli-unfold-argument  \
    --StartTime 2025-09-03T10:41:59+08:00 \
    --EndTime 2025-09-03T10:41:59+08:00 \
    --InstanceId crs-qjdkzsat \
    --Product redis \
    --Metric connections \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Host": "30.86.245.14",
                "InstanceProxyId": "149c8a81e5321ebab810a5da07c298c764311c43",
                "Port": 8461,
                "Series": [
                    {
                        "Metric": "cpu_util",
                        "Unit": "%",
                        "Values": [
                            0.4
                        ]
                    }
                ],
                "Timestamp": [
                    1758183175
                ],
                "Value": 1.33
            }
        ],
        "RequestId": "afc81d5e-499a-4800-b032-442fc0c4b7eb"
    }
}
```

