**Example 1: 查询负载均衡列表**

查询负载均衡列表。

Input: 

```
tccli teo DescribeLoadBalancerList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ZoneId zone-2ju9lrnpaxol
```

Output: 
```
{
    "Response": {
        "RequestId": "b8ecbb28-9360-4895-8138-668315e80b05",
        "LoadBalancerList": [
            {
                "FailoverPolicy": "OtherOriginGroup",
                "HealthChecker": {
                    "CriticalThreshold": 0,
                    "ExpectedCodes": [],
                    "FollowRedirect": "",
                    "Headers": [],
                    "HealthThreshold": 0,
                    "Interval": 0,
                    "Method": "",
                    "Path": "",
                    "Port": 0,
                    "RecvContext": "",
                    "SendContext": "",
                    "Timeout": 0,
                    "Type": "NoCheck"
                },
                "InstanceId": "lb-2my56s2a4fw7",
                "L4UsedList": [],
                "L7UsedList": [],
                "Name": "dyn-lb",
                "OriginGroupHealthStatus": [
                    {
                        "OriginGroupID": "og-30l5kv5z2bse",
                        "OriginGroupName": "allen_test_slave",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.12.231.49"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "43.137.35.174"
                            }
                        ],
                        "OriginType": "GENERAL",
                        "Priority": "priority_1"
                    },
                    {
                        "OriginGroupID": "og-30l5kv5z2ase",
                        "OriginGroupName": "allen_test_master",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.116.214.39"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "43.138.115.171"
                            }
                        ],
                        "OriginType": "GENERAL",
                        "Priority": "priority_2"
                    },
                    {
                        "OriginGroupID": "og-30l5kv5z2bsf",
                        "OriginGroupName": "test-origin",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.1.1.1"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "www.baidu.com"
                            }
                        ],
                        "OriginType": "GENERAL",
                        "Priority": "priority_3"
                    },
                    {
                        "OriginGroupID": "og-31l5kv5z2bsf",
                        "OriginGroupName": "origin-general",
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
                        "OriginType": "GENERAL",
                        "Priority": "priority_4"
                    }
                ],
                "Status": "Running",
                "SteeringPolicy": "Pritory",
                "Type": "GENERAL"
            },
            {
                "FailoverPolicy": "OtherOriginGroup",
                "HealthChecker": {
                    "CriticalThreshold": 2,
                    "ExpectedCodes": [],
                    "FollowRedirect": "",
                    "Headers": [],
                    "HealthThreshold": 3,
                    "Interval": 30,
                    "Method": "",
                    "Path": "",
                    "Port": 3344,
                    "RecvContext": "",
                    "SendContext": "",
                    "Timeout": 5,
                    "Type": "TCP"
                },
                "InstanceId": "lb-2my4ja5zzo1j",
                "L4UsedList": [],
                "L7UsedList": [],
                "Name": "pic-lb",
                "OriginGroupHealthStatus": [
                    {
                        "OriginGroupID": "og-30l5kv5z2bse",
                        "OriginGroupName": "allen_test_master",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.116.214.39"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "43.138.115.171"
                            }
                        ],
                        "OriginType": "GENERAL",
                        "Priority": "priority_1"
                    },
                    {
                        "OriginGroupID": "og-30l5kv5z2bse",
                        "OriginGroupName": "allen_test_slave",
                        "OriginHealthStatus": [
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "1.12.231.49"
                            },
                            {
                                "Healthy": "Unhealthy",
                                "Origin": "43.137.35.174"
                            }
                        ],
                        "OriginType": "GENERAL",
                        "Priority": "priority_2"
                    }
                ],
                "Status": "Running",
                "SteeringPolicy": "Pritory",
                "Type": "GENERAL"
            }
        ],
        "TotalCount": 2
    }
}
```

