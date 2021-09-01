**Example 1: 查询黑石物理机和虚机以及托管服务器绑定的黑石负载均衡详情**



Input: 

```
tccli bmlb DescribeDevicesBindInfo --cli-unfold-argument  \
    --InstanceIds cpm-buj66q9x \
    --VpcId vpc-34cxlz7z
```

Output: 
```
{
    "Response": {
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-14gtclwh",
                "AppId": 251000873,
                "ProjectId": 0,
                "VpcId": "vpc-34cxlz7z",
                "Vip": "115.159.240.22",
                "TgwSetType": "fullnat",
                "Exclusive": 0,
                "L4ListenerSet": [
                    {
                        "ListenerId": "lbl-f5wco8r3",
                        "Protocol": "tcp",
                        "LoadBalancerPort": 100,
                        "BackendSet": [
                            {
                                "InstanceId": "cpm-buj66q9x",
                                "Port": 111
                            }
                        ]
                    }
                ],
                "L7ListenerSet": [
                    {
                        "ListenerId": "lbl-lbbho4o3",
                        "Protocol": "https",
                        "LoadBalancerPort": 1580,
                        "RuleSet": [
                            {
                                "Domain": "bbb.com",
                                "DomainId": "dm-pt58nqp5",
                                "LocationSet": [
                                    {
                                        "Url": "/",
                                        "LocationId": "loc-oy3px9d7",
                                        "BackendSet": [
                                            {
                                                "InstanceId": "cpm-buj66q9x",
                                                "Port": 3333
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Domain": "ddd.com",
                                "DomainId": "dm-4z3kr9hn",
                                "LocationSet": [
                                    {
                                        "Url": "/",
                                        "LocationId": "loc-pia5k3lz",
                                        "BackendSet": [
                                            {
                                                "InstanceId": "cpm-buj66q9x",
                                                "Port": 2222
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "LoadBalancerId": "lb-q7qoi8cr",
                "AppId": 251000873,
                "ProjectId": 0,
                "VpcId": "vpc-34cxlz7z",
                "Vip": "115.159.240.89",
                "TgwSetType": "fullnat",
                "Exclusive": 0,
                "L4ListenerSet": [
                    {
                        "ListenerId": "lbl-rax7qrr7",
                        "Protocol": "tcp",
                        "LoadBalancerPort": 8000,
                        "BackendSet": [
                            {
                                "InstanceId": "cpm-buj66q9x",
                                "Port": 8000
                            },
                            {
                                "InstanceId": "cpm-buj66q9x",
                                "Port": 9000
                            }
                        ]
                    }
                ],
                "L7ListenerSet": [
                    {
                        "ListenerId": "lbl-4n8mp2dj",
                        "Protocol": "http",
                        "LoadBalancerPort": 80,
                        "RuleSet": [
                            {
                                "Domain": "a.com",
                                "DomainId": "dm-b358xyrr",
                                "LocationSet": [
                                    {
                                        "Url": "/",
                                        "LocationId": "loc-r0rcewj1",
                                        "BackendSet": [
                                            {
                                                "InstanceId": "cpm-buj66q9x",
                                                "Port": 80
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "d7f7f0dc-2d4d-4cc0-a97b-e13b14eaf4cc"
    }
}
```

