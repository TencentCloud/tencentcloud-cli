**Example 1: 创建转发规则**



Input: 

```
tccli privatedns CreateForwardRule --cli-unfold-argument  \
    --RuleType UP \
    --ZoneId zone-fadsvas \
    --RuleName 规则1 \
    --EndPointId eid-93kvksadf
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "RuleType": "UP",
        "RuleId": "fid-afdfaf2fsad",
        "ZoneId": "zone-fadsvas",
        "EndPointId": "eid-93kvksadf",
        "RuleName": "规则1"
    }
}
```

