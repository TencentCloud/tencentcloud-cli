**Example 1: 查询示例**



Input: 

```
tccli waf DescribeAttackWhiteRule --cli-unfold-argument  \
    --Domain xx \
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
                "MatchField": "xx",
                "MatchMethod": "xx",
                "MatchContent": "xx",
                "SignatureId": "xx",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "WhiteRuleId": 1,
                "CreateTime": "2020-09-22T00:00:00+00:00"
            },
            {
                "Status": 1,
                "MatchField": "xx",
                "MatchMethod": "xx",
                "MatchContent": "xx",
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

