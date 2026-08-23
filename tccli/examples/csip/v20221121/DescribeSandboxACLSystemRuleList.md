**Example 1: 查询 ACL 系统规则列表示例**



Input: 

```
tccli csip DescribeSandboxACLSystemRuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 1001,
                "RuleName": "禁止访问常见命令控制 IP",
                "RuleContent": [
                    {
                        "DstRule": {
                            "DstIP": [
                                "10.10.20.30",
                                "172.16.0.0/16"
                            ],
                            "DstIPExcept": [
                                "10.10.20.100"
                            ],
                            "DstPort": [
                                "443",
                                "8080-8090"
                            ],
                            "DstPortExcept": [
                                "22"
                            ]
                        },
                        "URLRule": {
                            "URL": [
                                "*.example.com",
                                "api.example.com/v1/*"
                            ],
                            "URLExcept": [
                                "test.example.com"
                            ],
                            "Protocol": [
                                "http",
                                "https"
                            ],
                            "Method": [
                                "GET",
                                "POST"
                            ]
                        }
                    }
                ]
            }
        ],
        "TotalCount": 32,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

