**Example 1: 查询HTTP监听器信息**



Input: 

```
tccli gaap DescribeHTTPListeners --cli-unfold-argument  \
    --ProxyId link-pl5ee4db \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3c48a850-4559-4132-8113-d075a235da2d",
        "TotalCount": 1,
        "ListenerSet": [
            {
                "ListenerId": "listener-kuwra6qh",
                "ListenerName": "listener-name",
                "Port": 80,
                "CreateTime": 1729568991,
                "Protocol": "HTTP",
                "ListenerStatus": 1,
                "ProxyId": "link-pl5ee4db",
                "GroupId": null
            }
        ]
    }
}
```

