**Example 1: 查询示例**



Input: 

```
tccli waf DescribeOpAttackWhiteRuleNew --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Order desc \
    --By CreateTime
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "Status": 0,
                "OpDomain": "www.test.com",
                "MatchField": "URL",
                "MatchMethod": "EXACT",
                "MatchContent": "",
                "OpAppId": "400000123",
                "SignatureId": "10000001",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "WhiteRuleId": 1,
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "48636a66-6b11-49c6-6603-b8f0c1428516"
    }
}
```

