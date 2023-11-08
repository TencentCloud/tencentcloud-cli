**Example 1: 查询防火墙模板规则列表**

查询防火墙模板规则列表

Input: 

```
tccli lighthouse DescribeFirewallTemplateRules --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy
```

Output: 
```
{
    "Response": {
        "RequestId": "8e3d057f-a651-4c66-b5e3-abb11e305f19",
        "TemplateRuleSet": [
            {
                "FirewallRuleInfo": {
                    "Action": "ACCEPT",
                    "AppType": "user-defined",
                    "CidrBlock": "0.0.0.0/0",
                    "FirewallRuleDescription": "tcp 80",
                    "Port": "81",
                    "Protocol": "TCP"
                },
                "TemplateRuleId": "lhftr-gexf7cmvpq"
            },
            {
                "FirewallRuleInfo": {
                    "Action": "DROP",
                    "AppType": "user-defined",
                    "CidrBlock": "0.0.0.0/0",
                    "FirewallRuleDescription": "udp 80",
                    "Port": "81",
                    "Protocol": "UDP"
                },
                "TemplateRuleId": "lhftr-9uxz9zuz62"
            }
        ],
        "TotalCount": 2
    }
}
```

