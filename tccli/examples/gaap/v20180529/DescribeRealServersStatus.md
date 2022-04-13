**Example 1: 查询源站绑定状态**

查询源站绑定状态

Input: 

```
tccli gaap DescribeRealServersStatus --cli-unfold-argument  \
    --RealServerIds rs-4ftghy6
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "RealServerStatusSet": [
            {
                "ProxyId": "xx",
                "BindStatus": 0,
                "RealServerId": "xx",
                "GroupId": "xx"
            }
        ]
    }
}
```

