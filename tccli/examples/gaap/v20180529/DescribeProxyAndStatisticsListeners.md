**Example 1: 查询统计通道和监听器信息**



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
                "ListenerList": [],
                "ProxyId": "link-1oczk2c3",
                "ProxyName": "default"
            }
        ],
        "TotalCount": 34,
        "RequestId": "c931b2ef-0fef-4d2f-92d8-90463cf2ed2b"
    }
}
```

