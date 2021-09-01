**Example 1: 搜索规则**



Input: 

```
tccli iotexplorer SearchTopicRule --cli-unfold-argument  \
    --RuleName test_create
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

