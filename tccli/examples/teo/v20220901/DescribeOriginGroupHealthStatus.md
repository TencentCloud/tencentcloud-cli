**Example 1: 查询负载均衡实例下源站健康状态**

查询负载均衡实例下源站健康状态。


Input: 

```
tccli teo DescribeOriginGroupHealthStatus --cli-unfold-argument  \
    --ZoneId zone-2ju9lrmqaxol \
    --LBInstanceId lb-2mzy6je01y82 \
    --OriginGroupIds og-30l5kv5z2bse
```

Output: 
```
{
    "Response": {
        "RequestId": "2b891f6f-3317-4c31-a1dd-5b2e53eaae4e",
        "OriginGroupHealthStatusList": [
            {
                "CheckRegionHealthStatus": [
                    {
                        "Healthy": "Unhealthy",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "2.2.2.2"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.1.1.1"
                            }
                        ],
                        "Region": "BR-SP"
                    },
                    {
                        "Healthy": "Unhealthy",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "2.2.2.2"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.1.1.1"
                            }
                        ],
                        "Region": "CN-JX"
                    },
                    {
                        "Healthy": "Unhealthy",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "2.2.2.2"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.1.1.1"
                            }
                        ],
                        "Region": "NL-NH"
                    },
                    {
                        "Healthy": "Unhealthy",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.1.1.1"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "2.2.2.2"
                            }
                        ],
                        "Region": "CN-SD"
                    },
                    {
                        "Healthy": "Unhealthy",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "2.2.2.2"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.1.1.1"
                            }
                        ],
                        "Region": "US-FL"
                    }
                ],
                "OriginGroupId": "og-30l5kv5z2bse",
                "OriginHealthStatus": [
                    {
                        "Healthy": "Unhealthy",
                        "Origin": "2.2.2.2"
                    },
                    {
                        "Healthy": "Unhealthy",
                        "Origin": "1.1.1.1"
                    }
                ]
            }
        ]
    }
}
```

