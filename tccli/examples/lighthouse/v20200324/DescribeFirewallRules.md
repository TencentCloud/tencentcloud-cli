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
        "FirewallRuleSet": [
            {
                "Action": "DROP",
                "AppType": "自定义",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "",
                "Port": "22,88",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "自定义",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "test",
                "Port": "88",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "HTTP(80)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "test",
                "Port": "80",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "HTTPS(443)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通Web服务HTTPS(443)，如 Apache、Nginx",
                "Port": "443",
                "Protocol": "TCP"
            }
        ],
        "FirewallVersion": 1,
        "RequestId": "afa0c876-336a-4ed6-ad01-89b3b2632207",
        "TotalCount": 4
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
        "FirewallRuleSet": [
            {
                "Action": "DROP",
                "AppType": "自定义",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "",
                "Port": "22,88",
                "Protocol": "TCP"
            }
        ],
        "FirewallVersion": 1,
        "RequestId": "31522fb9-fef8-4190-9080-deba504c36ae",
        "TotalCount": 4
    }
}
```

