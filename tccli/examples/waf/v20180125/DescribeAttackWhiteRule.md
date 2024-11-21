**Example 1: 查询示例**



Input: 

```
tccli waf DescribeAttackWhiteRule --cli-unfold-argument  \
    --Domain test.domain.com \
    --Offset 0 \
    --Limit 10 \
    --Order dsc \
    --By modify_time
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "WhiteRuleId": 14931,
                "Name": "whiteRuleName",
                "SignatureId": "30000163",
                "SignatureIds": [
                    "30000163"
                ],
                "TypeId": "01000000",
                "TypeIds": [
                    "10000001"
                ],
                "Mode": 0,
                "Status": 1,
                "MatchField": "URL",
                "MatchMethod": "eq",
                "MatchContent": "/asdfad",
                "MatchInfo": [
                    {
                        "MatchField": "URL",
                        "MatchMethod": "eq",
                        "MatchContent": "/asdfad"
                    }
                ],
                "MatchInfoStr": "[{\"MatchField\":\"URL\",\"MatchParams\":\"\",\"MatchMethod\":\"eq\",\"MatchContent\":\"/asdfad\"}]",
                "CreateTime": "2024-10-29T21:19:12+08:00",
                "ModifyTime": "2024-10-29T21:19:12+08:00"
            }
        ],
        "RequestId": "d3f9fc57-dbfd-4503-ad95-eab902c6257c"
    }
}
```

