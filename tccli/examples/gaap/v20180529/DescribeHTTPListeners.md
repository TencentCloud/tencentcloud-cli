**Example 1: 查询HTTP监听器信息**



Input: 

```
tccli gaap DescribeHTTPListeners --cli-unfold-argument  \
    --ProxyId link-p9888rix \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "CreateTime": 1768205444,
                "GroupId": null,
                "ListenerId": "listener-9vub5ymx",
                "ListenerName": "listener-name",
                "ListenerStatus": 0,
                "Port": 8091,
                "Protocol": "HTTP",
                "ProxyId": "link-p9888rix"
            }
        ],
        "TotalCount": 1,
        "RequestId": "b101e45d-34ea-44e8-b735-b0c5487a7ae1"
    }
}
```

