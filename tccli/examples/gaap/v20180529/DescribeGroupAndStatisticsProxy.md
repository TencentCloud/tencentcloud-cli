**Example 1: 查询统计通道组和通道信息**

查询统计通道组和通道信息

Input: 

```
tccli gaap DescribeGroupAndStatisticsProxy --cli-unfold-argument  \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "GroupSet": [
            {
                "GroupId": "lg-r737geg",
                "GroupName": "lg-test",
                "ProxySet": [
                    {
                        "ProxyId": "link-mmu241ob",
                        "ProxyName": "link-test",
                        "ListenerList": [
                            {
                                "ListenerId": "listener-lmifrrmh",
                                "ListenerName": "linstener-test",
                                "Port": 80,
                                "Protocol": "HTTP"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

