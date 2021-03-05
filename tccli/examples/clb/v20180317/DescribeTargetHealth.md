**Example 1: 查询负载均衡实例的后端健康状态**



Input: 

```
tccli clb DescribeTargetHealth --cli-unfold-argument  \
    --LoadBalancerIds lb-qc2iq5yc
```

Output: 
```
{
    "Response": {
        "LoadBalancers": [
            {
                "Listeners": [
                    {
                        "Rules": [
                            {
                                "Url": "/",
                                "Domain": "www.123.com",
                                "LocationId": "loc-5t7526km",
                                "Targets": []
                            }
                        ],
                        "Port": 666,
                        "Protocol": "HTTP",
                        "ListenerId": "lbl-j36caqde",
                        "ListenerName": "http-111"
                    },
                    {
                        "Rules": [
                            {
                                "Url": null,
                                "Domain": null,
                                "LocationId": "loc-ewygg6i0",
                                "Targets": [
                                    {
                                        "HealthStatus": false,
                                        "IP": "172.16.0.6",
                                        "TargetId": "ins-19425500",
                                        "Port": 2020
                                    },
                                    {
                                        "HealthStatus": true,
                                        "IP": "172.16.0.12",
                                        "TargetId": "ins-19425y2y",
                                        "Port": 80
                                    }
                                ]
                            }
                        ],
                        "Port": 789,
                        "Protocol": "TCP",
                        "ListenerId": "lbl-fs9naq76",
                        "ListenerName": "tcp_test"
                    },
                    {
                        "Rules": [
                            {
                                "Url": "/",
                                "Domain": "www.456.com",
                                "LocationId": "loc-8gdc4qcq",
                                "Targets": []
                            }
                        ],
                        "Port": 777,
                        "Protocol": "HTTP",
                        "ListenerId": "lbl-9nj07x0m",
                        "ListenerName": "http-222"
                    },
                    {
                        "Rules": [],
                        "Port": 1949,
                        "Protocol": "HTTPS",
                        "ListenerId": "lbl-087wrv48",
                        "ListenerName": "https-000"
                    }
                ],
                "LoadBalancerName": "lb-test123",
                "LoadBalancerId": "lb-qc2iq5yc"
            }
        ],
        "RequestId": "9d45e1ec-720c-4ce1-860e-e338e273e77e"
    }
}
```

