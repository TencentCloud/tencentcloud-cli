**Example 1: Web托管日志入参**



Input: 

```
tccli teo DescribeWebManagedRulesLog --cli-unfold-argument  \
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
                    "Domain": "xx",
                    "SipCountryCode": "xx",
                    "AttackIp": "xx",
                    "RiskLevel": "xx",
                    "RequestUri": "xx",
                    "RuleId": 1,
                    "AttackContent": "xx",
                    "RequestMethod": "xx",
                    "Msuuid": "xx",
                    "AttackTime": 1,
                    "AttackType": "xx",
                    "DisposalMethod": "xx",
                    "Ua": "xx"
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

