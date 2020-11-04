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
        "RealServerStatusSet": [
            {
                "RealServerId": "rs-4ftghy6",
                "BindStatus": 0,
                "ProxyId": "link-asfke"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

