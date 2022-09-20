**Example 1: 查询Web攻击日志**



Input: 

```
tccli teo DescribeWebManagedRulesLog --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "EventId": "18045868509676540160",
                "HttpLog": "{\"PROTOCOL\":\"HTTP/1.1\"}",
                "Domain": "www.baidu.com",
                "SipCountryCode": "CN",
                "AttackIp": "120.241.137.74",
                "RequestUri": "/waf",
                "RuleDetailList": [
                    {
                        "Description": "针对出现在GET参数中的命令注入防护规则",
                        "RuleId": 106247153,
                        "RiskLevel": "high risk",
                        "RuleTypeName": "命令/代码注入攻击防护",
                        "Action": "monitor",
                        "RuleLevel": "严格"
                    }
                ],
                "AttackTime": 1660033867
            }
        ],
        "RequestId": "dd54b175-5594-4acc-a230-75d8ae19b5bf"
    }
}
```

