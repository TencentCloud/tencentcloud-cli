**Example 1: 查找绑定了某主机或者有某转发域名黑石负载均衡七层监听器**



Input: 

```
tccli bmlb DescribeL7ListenerInfo --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --IfGetBackendInfo 1
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "lbl-n0sfq477",
                "ListenerName": "5555",
                "Protocol": "http",
                "LoadBalancerPort": 81,
                "Bandwidth": 0,
                "ListenerType": "L7Listener",
                "SslMode": 0,
                "CertId": "",
                "CertCaId": "",
                "Status": 1,
                "AddTimestamp": "2018-11-06 15:01:49",
                "RuleSet": [
                    {
                        "Domain": "e.com",
                        "DomainId": "dm-cqllxlnn",
                        "Status": 1,
                        "AddTimestamp": "2018-11-06 16:32:00",
                        "LocationSet": [
                            {
                                "Url": "/a/b/c",
                                "LocationId": "loc-2l0fj4ix",
                                "SessionExpire": 30,
                                "HealthSwitch": 1,
                                "HttpCheckPath": "/a/",
                                "HttpCheckDomain": "",
                                "IntervalTime": 60,
                                "HealthNum": 6,
                                "UnhealthNum": 5,
                                "HttpCodes": [
                                    3,
                                    4
                                ],
                                "BalanceMode": "wrr",
                                "Status": 1,
                                "AddTimestamp": "2018-11-06 16:32:00",
                                "BackendSet": [
                                    {
                                        "BindType": 0,
                                        "InstanceId": "cpm-buj66q9x",
                                        "Alias": "（测试长期占用）amizhang-tgw测试-勿动",
                                        "LanIp": "10.10.1.3",
                                        "Port": 100,
                                        "Weight": 88,
                                        "Status": "Dead"
                                    },
                                    {
                                        "BindType": 1,
                                        "InstanceId": "",
                                        "Alias": "",
                                        "LanIp": "10.10.1.6",
                                        "Port": 66,
                                        "Weight": 100,
                                        "Status": "Dead"
                                    },
                                    {
                                        "BindType": 1,
                                        "InstanceId": "",
                                        "Alias": "",
                                        "LanIp": "10.10.1.7",
                                        "Port": 66,
                                        "Weight": 10,
                                        "Status": "Dead"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "a3f7b4f4-a17d-4483-a93f-ab7d698e68b1"
    }
}
```

