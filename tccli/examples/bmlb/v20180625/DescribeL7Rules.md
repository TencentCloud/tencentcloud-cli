**Example 1: 获取黑石负载均衡七层转发规则**



Input: 

```
tccli bmlb DescribeL7Rules --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5
```

Output: 
```
{
    "Response": {
        "RuleSet": [
            {
                "Domain": "b.com",
                "DomainId": "dm-ftaez2bl",
                "Status": 1,
                "AddTimestamp": "2018-11-06 15:45:12",
                "LocationSet": [
                    {
                        "Url": "/",
                        "LocationId": "loc-bwxdimq5",
                        "SessionExpire": 0,
                        "HealthSwitch": 1,
                        "HttpCheckPath": "/a/",
                        "HttpCheckDomain": "b.com",
                        "IntervalTime": 30,
                        "HealthNum": 3,
                        "UnhealthNum": 3,
                        "HttpCodes": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "BalanceMode": "wrr",
                        "Status": 1,
                        "AddTimestamp": "2018-11-06 15:45:12"
                    }
                ]
            },
            {
                "Domain": "c.com",
                "DomainId": "dm-mq3qr5v3",
                "Status": 1,
                "AddTimestamp": "2018-11-06 15:56:58",
                "LocationSet": [
                    {
                        "Url": "/",
                        "LocationId": "loc-rm84yp9j",
                        "SessionExpire": 0,
                        "HealthSwitch": 1,
                        "HttpCheckPath": "/a/",
                        "HttpCheckDomain": "c.com",
                        "IntervalTime": 30,
                        "HealthNum": 3,
                        "UnhealthNum": 3,
                        "HttpCodes": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "BalanceMode": "wrr",
                        "Status": 1,
                        "AddTimestamp": "2018-11-06 15:56:58"
                    }
                ]
            },
            {
                "Domain": "d.com",
                "DomainId": "dm-eih4t7tx",
                "Status": 1,
                "AddTimestamp": "2018-11-06 16:17:24",
                "LocationSet": [
                    {
                        "Url": "/",
                        "LocationId": "loc-a91atsct",
                        "SessionExpire": 0,
                        "HealthSwitch": 1,
                        "HttpCheckPath": "/a/",
                        "HttpCheckDomain": "d.com",
                        "IntervalTime": 30,
                        "HealthNum": 3,
                        "UnhealthNum": 3,
                        "HttpCodes": [
                            1
                        ],
                        "BalanceMode": "wrr",
                        "Status": 1,
                        "AddTimestamp": "2018-11-06 16:17:24"
                    }
                ]
            },
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
                        "HttpCheckDomain": "e.com",
                        "IntervalTime": 60,
                        "HealthNum": 6,
                        "UnhealthNum": 6,
                        "HttpCodes": [
                            3,
                            4
                        ],
                        "BalanceMode": "wrr",
                        "Status": 1,
                        "AddTimestamp": "2018-11-06 16:32:00"
                    }
                ]
            }
        ],
        "RequestId": "4576214f-c836-4579-9542-bbbe0a69c839"
    }
}
```

