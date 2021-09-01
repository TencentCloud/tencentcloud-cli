**Example 1: 查询规则列表**



Input: 

```
tccli gpm DescribeRules --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --SearchType ruleCode \
    --Keyword rule-r4x6tk49
```

Output: 
```
{
    "Response": {
        "Keyword": "rule-r4x6tk49",
        "PageNumber": 1,
        "PageSize": 10,
        "RequestId": "a2719713-1ee9-4a67-894a-e776fa52d203",
        "RuleInfoList": [
            {
                "CreateTime": "2020-09-29 10:52:48",
                "MatchCodeList": [
                    {
                        "Key": "match-74w0ckl8",
                        "Value": "test"
                    }
                ],
                "RuleCode": "rule-r4x6tk49",
                "RuleName": "test"
            }
        ],
        "SearchType": "ruleCode",
        "TotalCount": 1
    }
}
```

