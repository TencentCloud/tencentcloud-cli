**Example 1: 获取CC防护的访问频率控制规则**



Input: 

```
tccli dayu DescribeCCFrequencyRules --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleId rule-0000001
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "CCFrequencyRuleList": [
            {
                "CCFrequencyRuleId": "ccRule-0000001i",
                "Uri": "/",
                "UserAgent": "",
                "Cookie": "",
                "Mode": "include",
                "Period": 10,
                "ReqNumber": 1,
                "Act": "drop",
                "ExeDuration": 1
            }
        ],
        "CCFrequencyRuleStatus": "on"
    }
}
```

