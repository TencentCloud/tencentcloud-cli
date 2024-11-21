**Example 1: 根据URL查询API规则**



Input: 

```
tccli waf DescribeCCRuleList --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Limit 1 \
    --Filters.0.Values clb saas \
    --Filters.0.Name InstanceType \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --By ts_version
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "ActionType": 22,
                    "Advance": 0,
                    "Interval": 60,
                    "Limit": 60,
                    "MatchFunc": 0,
                    "Name": "ccRuleName",
                    "Priority": 50,
                    "Options": "[{\"key\":\"Post\",\"args\":[\"a2V5YQ=dmFsdWVh\"],\"match\":\"0\",\"encodeflag\":true}]",
                    "Status": 1,
                    "TsVersion": 1579058116920,
                    "Url": "///",
                    "ValidTime": 600,
                    "RuleId": 1900009616,
                    "EventId": "12983ac"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "1cc54bf4-cfeb-40cc-a823-035e52106df9"
    }
}
```

