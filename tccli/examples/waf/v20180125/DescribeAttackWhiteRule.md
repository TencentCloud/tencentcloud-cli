**Example 1: 查询示例**



Input: 

```
tccli waf DescribeAttackWhiteRule --cli-unfold-argument  \
    --Domain  \
    --Offset 1 \
    --Limit 1 \
    --Order  \
    --By 
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "WhiteRuleId": 1,
                "SignatureId": "abc",
                "Status": 0,
                "MatchField": "abc",
                "MatchParams": "abc",
                "MatchMethod": "abc",
                "MatchContent": "abc",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "SignatureIds": [
                    "abc"
                ],
                "TypeIds": [
                    "abc"
                ],
                "TypeId": "abc",
                "Mode": 0,
                "Name": "abc",
                "MatchInfo": [
                    {
                        "MatchField": "abc",
                        "MatchMethod": "abc",
                        "MatchContent": "abc",
                        "MatchParams": "abc"
                    }
                ],
                "MatchInfoStr": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

