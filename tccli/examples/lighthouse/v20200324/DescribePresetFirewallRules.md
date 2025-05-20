**Example 1: 查询预设防火墙规则列表**

查询预设防火墙规则列表

Input: 

```
tccli lighthouse DescribePresetFirewallRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FirewallRuleSet": [
            {
                "Action": "ACCEPT",
                "AppType": "Windows login (3389)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "Windows remote desktop login",
                "Port": "3389",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "Windows login optimization (3389)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "Optimize Windows remote desktop login experience",
                "Port": "3389",
                "Protocol": "UDP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "Linux login (22)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "Linux SSH login",
                "Port": "22",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "FTP (21)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "FTP service (21)",
                "Port": "21",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "HTTP (80)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "Web HTTP service (80), such as Apache, Nginx, etc.",
                "Port": "80",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "HTTPS (443)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "Web HTTPS service (443), such as Apache, Nginx, etc.",
                "Port": "443",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "MySQL (3306)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "MySQL database service (3306)",
                "Port": "3306",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "SQL Server (1433)",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "SQL Server database service (1433)",
                "Port": "1433",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "All TCP",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "All TCP",
                "Port": "1-65535",
                "Protocol": "TCP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "All UDP",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "All UDP",
                "Port": "1-65535",
                "Protocol": "UDP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "Ping",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "Use Ping to test network connectivity (Allow ALL ICMP)",
                "Port": "ALL",
                "Protocol": "ICMP"
            },
            {
                "Action": "ACCEPT",
                "AppType": "ALL",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "All TCP、UDP、ICMP and GRE",
                "Port": "ALL",
                "Protocol": "ALL"
            }
        ],
        "RequestId": "254770cd-c72c-46e3-a634-900980a89f3c",
        "TotalCount": 12
    }
}
```

