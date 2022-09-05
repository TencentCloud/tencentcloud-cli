**Example 1: 查询waf攻击日志**



Input: 

```
tccli teo DescribeWebManagedRulesLog --cli-unfold-argument  \
    --PageSize 1 \
    --PageNo 1 \
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
        "Status": 0,
        "Msg": "success",
        "Data": {
            "TotalSize": 1,
            "List": [
                {
                    "EventId": "18045868509676540160",
                    "HttpLog": "{\"PROTOCOL\":\"HTTP/1.1\"}",
                    "Domain": "www.baidu.com",
                    "SipCountryCode": "CN",
                    "AttackIp": "120.241.137.74",
                    "RequestUri": "/waf",
                    "RuleId": 1,
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
            "PageSize": 1,
            "PageNo": 1,
            "Pages": 1
        },
        "RequestId": "dd54b175-5594-4acc-a230-75d8ae19b5bf"
    }
}
```

