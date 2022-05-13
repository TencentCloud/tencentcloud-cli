**Example 1: 查询示例**



Input: 

```
tccli waf DescribeOpAttackWhiteRuleNew --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Order xx \
    --By xx
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "Status": 0,
                "OpDomain": "xx",
                "MatchField": "xx",
                "MatchMethod": "xx",
                "MatchContent": "xx",
                "OpAppId": "xx",
                "SignatureId": "xx",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "WhiteRuleId": 1,
                "CreateTime": "2020-09-22T00:00:00+00:00"
            },
            {
                "Status": 1,
                "OpDomain": "xx",
                "MatchField": "xx",
                "MatchMethod": "xx",
                "MatchContent": "xx",
                "OpAppId": "xx",
                "SignatureId": "xx",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "WhiteRuleId": 1,
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

