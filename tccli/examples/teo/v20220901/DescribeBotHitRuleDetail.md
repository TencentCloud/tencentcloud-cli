**Example 1: 查询Bot攻击命中规则详情**



Input: 

```
tccli teo DescribeBotHitRuleDetail --cli-unfold-argument  \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --Limit 1 \
    --Offset 0 \
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
        "TotalCount": 2,
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "Data": [
            {
                "Description": "站点监控",
                "RuleId": 1659,
                "ZoneId": "zone-2c2jrfftg9mh",
                "RequestNum": 22,
                "Action": "monitor",
                "HitTime": 1659597382,
                "AlarmEnabled": true,
                "RuleEnabled": true,
                "RuleDeleted": false
            }
        ]
    }
}
```

