**Example 1: 获取规则列表**



Input: 

```
tccli iotexplorer GetTopicRuleList --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68",
        "Rules": [
            {
                "RuleName": "test_create",
                "Description": "test",
                "CreatedAt": 1599017883,
                "RuleDisabled": true
            }
        ],
        "TotalCnt": 1
    }
}
```

