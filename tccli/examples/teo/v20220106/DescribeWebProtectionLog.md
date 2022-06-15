**Example 1: 限速拦截日志**



Input: 

```
tccli teo DescribeWebProtectionLog --cli-unfold-argument  \
    --ZoneIds zoneId1 zoneId2 \
    --Domains www.baidu.com \
    --QueryCondition.0.Key key test \
    --QueryCondition.0.Operator operator test \
    --QueryCondition.0.Value v1 v2 \
    --StartTime 2020-04-30T00:00:00Z \
    --EndTime 2020-04-30T00:00:00Z \
    --PageSize 2 \
    --PageNo 1
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "xx",
        "Data": {
            "TotalSize": 0,
            "List": [
                {
                    "EventId": "xx",
                    "HttpLog": "xx",
                    "SipCountryCode": "xx",
                    "RuleId": 1,
                    "RiskLevel": "xx",
                    "RequestUri": "xx",
                    "AttackDomain": "xx",
                    "AttackTime": 1,
                    "DisposalMethod": "xx",
                    "HitCount": 1,
                    "AttackSip": "xx"
                }
            ],
            "PageSize": 0,
            "PageNo": 0,
            "Pages": 0
        },
        "RequestId": "xx"
    }
}
```

