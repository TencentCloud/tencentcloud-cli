**Example 1: 查询cc防护命中规则详情**



Input: 

```
tccli teo DescribeWebProtectionHitRuleDetail --cli-unfold-argument  \
    --EntityType acl \
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
        "RequestId": "a55ce448-d5e6-4351-9a1f-8f0a5222fba1",
        "Data": [
            {
                "Description": "cooper5_rate",
                "RuleId": 1234,
                "ZoneId": "zone-2c2jrfftg9mh",
                "RequestNum": 10,
                "Action": "monitor",
                "HitTime": 1660035802,
                "AlarmEnabled": true,
                "RuleEnabled": false,
                "RuleDeleted": false
            }
        ]
    }
}
```

