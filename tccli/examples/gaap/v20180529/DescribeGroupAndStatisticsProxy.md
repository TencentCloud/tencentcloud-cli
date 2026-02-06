**Example 1: 查询统计通道组和通道信息**



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
                "GroupId": "lg-0o223et7",
                "GroupName": "group-name",
                "ProxySet": [
                    {
                        "ListenerList": [
                            {
                                "ListenerId": "listener-3jebyh2r",
                                "ListenerName": "wins",
                                "Port": 443,
                                "Protocol": "HTTPS"
                            }
                        ],
                        "ProxyId": "link-eagpfyhh",
                        "ProxyName": "default"
                    }
                ]
            }
        ],
        "TotalCount": 17,
        "RequestId": "15045f88-6867-4896-acf1-c08872084933"
    }
}
```

