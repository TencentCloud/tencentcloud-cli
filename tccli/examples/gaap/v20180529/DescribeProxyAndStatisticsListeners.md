**Example 1: 查询统计通道和监听器信息**

查询统计通道和监听器信息

Input: 

```
tccli gaap DescribeProxyAndStatisticsListeners --cli-unfold-argument  \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "ProxySet": [
            {
                "ProxyId": "link-mmu241ob",
                "ProxyName": "wegame",
                "ListenerList": [
                    {
                        "ListenerId": "listener-lmifrrmh",
                        "ListenerName": "wegame",
                        "Protocol": "HTTP",
                        "Port": 80
                    }
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

