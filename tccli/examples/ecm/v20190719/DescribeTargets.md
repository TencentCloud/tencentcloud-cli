**Example 1: 查询负载均衡绑定的后端服务列表**



Input: 

```
tccli ecm DescribeTargets --cli-unfold-argument  \
    --LoadBalancerId lb-f9zyj3kb
```

Output: 
```
{
    "Response": {
        "RequestId": "cbc4f5bf-589e-4102-a608-bef958372313",
        "Listeners": [
            {
                "Targets": [],
                "ListenerId": "lbl-43jbp1cc",
                "Port": 12345,
                "Protocol": "TCP"
            },
            {
                "Targets": [],
                "ListenerId": "lbl-aznj4uuk",
                "Port": 222,
                "Protocol": "TCP"
            },
            {
                "Targets": [
                    {
                        "EniId": "eni-i0qls00b",
                        "InstanceName": "",
                        "InstanceId": "ein-nu5sp1s4",
                        "PublicIpAddresses": [
                            "101.67.8.124"
                        ],
                        "Port": 23001,
                        "RegisteredTime": "2020-08-12 16:08:15",
                        "Weight": 100,
                        "PrivateIpAddresses": [
                            "172.16.0.74"
                        ]
                    },
                    {
                        "EniId": "eni-55sj7ug9",
                        "InstanceName": "低调的测试机",
                        "InstanceId": "ein-dqvc6c5g",
                        "PublicIpAddresses": [
                            "101.67.8.111"
                        ],
                        "Port": 23001,
                        "RegisteredTime": "2020-08-12 16:08:15",
                        "Weight": 100,
                        "PrivateIpAddresses": [
                            "172.16.0.11"
                        ]
                    }
                ],
                "ListenerId": "lbl-o0hptbhg",
                "Port": 13001,
                "Protocol": "TCP"
            },
            {
                "Targets": [
                    {
                        "EniId": "eni-i0qls00b",
                        "InstanceName": "",
                        "InstanceId": "ein-nu5sp1s4",
                        "PublicIpAddresses": [
                            "101.67.8.124"
                        ],
                        "Port": 23002,
                        "RegisteredTime": "2020-08-12 16:10:41",
                        "Weight": 100,
                        "PrivateIpAddresses": [
                            "172.16.0.74"
                        ]
                    },
                    {
                        "EniId": "eni-i0qls00b",
                        "InstanceName": "",
                        "InstanceId": "ein-nu5sp1s4",
                        "PublicIpAddresses": [
                            "101.67.8.124"
                        ],
                        "Port": 23012,
                        "RegisteredTime": "2020-08-12 16:10:41",
                        "Weight": 100,
                        "PrivateIpAddresses": [
                            "172.16.0.74"
                        ]
                    }
                ],
                "ListenerId": "lbl-jruukfae",
                "Port": 13002,
                "Protocol": "TCP"
            },
            {
                "Targets": [],
                "ListenerId": "lbl-6p9gf1nq",
                "Port": 13003,
                "Protocol": "TCP"
            }
        ]
    }
}
```

