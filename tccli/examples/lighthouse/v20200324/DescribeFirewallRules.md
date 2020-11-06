**Example 1: 查询实例的所有防火墙规则**



Input: 

```
tccli lighthouse DescribeFirewallRules --cli-unfold-argument  \
    --InstanceId lhins-aglzynfg
```

Output: 
```
{
    "Response": {
        "TotalCount": 7,
        "FirewallRuleSet": [
            {
                "AppType": "HTTP(80)",
                "Protocol": "TCP",
                "Port": "80"
            },
            {
                "AppType": "HTTPS(443)",
                "Protocol": "TCP",
                "Port": "443"
            },
            {
                "AppType": "Linux登录(22)",
                "Protocol": "TCP",
                "Port": "22"
            },
            {
                "AppType": "Windows登录(3389)",
                "Protocol": "TCP",
                "Port": "3389"
            },
            {
                "AppType": "自定义",
                "Protocol": "TCP",
                "Port": "300"
            },
            {
                "AppType": "自定义",
                "Protocol": "TCP",
                "Port": "84-90"
            },
            {
                "AppType": "自定义",
                "Protocol": "TCP",
                "Port": "85,92"
            }
        ],
        "RequestId": "a41e2048-82c8-4d43-826a-9f6a5b23d3e5"
    }
}
```

**Example 2: 查询实例的部分防火墙规则**



Input: 

```
tccli lighthouse DescribeFirewallRules --cli-unfold-argument  \
    --InstanceId lhins-aglzynfg \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 7,
        "FirewallRuleSet": [
            {
                "AppType": "HTTP(80)",
                "Protocol": "TCP",
                "Port": "80"
            }
        ],
        "RequestId": "28308810-42e6-4ee4-98d7-14471ae149a4"
    }
}
```

