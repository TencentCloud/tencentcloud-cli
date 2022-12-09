**Example 1: 查询Web攻击命中规则详情**



Input: 

```
tccli teo DescribeWebManagedRulesHitRuleDetail --cli-unfold-argument  \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --Limit 1 \
    --Offset 1 \
    --Interval min \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "Data": [
            {
                "Description": "针对出现在GET参数中的命令注入防护规则",
                "RuleId": 106247153,
                "ZoneId": "zone-2c2jrfftg9mh",
                "RequestNum": 10,
                "Action": "monitor",
                "HitTime": 1659690912,
                "BotLabel": "none",
                "AlarmEnabled": true,
                "RuleEnabled": true,
                "RuleDeleted": false
            }
        ]
    }
}
```

