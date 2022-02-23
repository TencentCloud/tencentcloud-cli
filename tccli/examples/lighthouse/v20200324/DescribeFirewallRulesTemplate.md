**Example 1: 查询防火墙规则模板**



Input: 

```
tccli lighthouse DescribeFirewallRulesTemplate --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FirewallRuleSet": [
            {
                "Action": "ACCEPT",
                "AppType": "Windows登录(3389)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通Windows远程登录",
                "Port": "3389",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "Linux登录(22)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通Linux SSH登录",
                "Port": "22",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "HTTP(80)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通Web服务HTTP(80)，如 Apache、Nginx",
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
            },
            {
                "Action": "ACCEPT",
                "AppType": "MySQL(3306)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通MySQL服务(3306)",
                "Port": "3306",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "SQL Server(1433)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通SQL Server服务(1433)",
                "Port": "1433",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "全部TCP",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通全部TCP",
                "Port": "1-65535",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "全部UDP",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通全部UDP",
                "Port": "1-65535",
                "Protocol": "UDP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "Ping-ICMP",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通Ping",
                "Port": "ALL",
                "Protocol": "ICMP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "ALL",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "放通全部TCP、UDP、ICMP(Ping)以及GRE",
                "Port": "ALL",
                "Protocol": "ALL"
            }
        ],
        "RequestId": "b9fdb7cc-8afa-4fae-9062-73e41d06f7d3",
        "TotalCount": 10
    }
}
```

