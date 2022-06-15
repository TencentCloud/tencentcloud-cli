**Example 1: Bot攻击日志**



Input: 

```
tccli teo DescribeBotLog --cli-unfold-argument  \
    --PageSize 0 \
    --PageNo 0 \
    --ZoneIds xx \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains xx \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --QueryCondition.0.Operator xx \
    --QueryCondition.0.Value xx \
    --QueryCondition.0.Key xx
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
                    "Confidence": "xx",
                    "AttackContent": "xx",
                    "RequestMethod": "xx",
                    "Maliciousness": "xx",
                    "AttackTime": 1,
                    "AttackType": "xx",
                    "DisposalMethod": "xx",
                    "DetectionMethod": "xx",
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

