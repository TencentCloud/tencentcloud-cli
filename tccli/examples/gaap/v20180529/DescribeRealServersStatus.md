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
        "RequestId": "dad2a717-3c7d-444d-8f98-0cca9c897ff3",
        "RealServerStatusSet": [
            {
                "ProxyId": "link-123456",
                "BindStatus": 0,
                "RealServerId": "rs-123456",
                "GroupId": "lg-123456"
            }
        ]
    }
}
```

