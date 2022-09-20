**Example 1: 查询域名学习到的智能客户端规则**



Input: 

```
tccli teo DescribeRateLimitIntelligenceRule --cli-unfold-argument  \
    --Entity www.example.com \
    --ZoneId zone-w28fh20f
```

Output: 
```
{
    "Response": {
        "RateLimitIntelligenceRuleDetails": [
            {
                "Status": "allow",
                "RuleId": 1,
                "EffectiveTime": "2020-09-22T00:00:00+00:00",
                "MatchContent": "1.1.1.1",
                "ExpireTime": "2020-09-22T00:00:00+00:00",
                "Action": "monitor"
            }
        ],
        "RequestId": "3jca0ffj2-3d29024f-2kdfcfsnr9"
    }
}
```

