**Example 1: 获取规则列表示例**



Input: 

```
tccli iotcloud ListTopicRules --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCnt": 2,
        "Rules": [
            {
                "RuleName": "rule2",
                "CreatedAt": 1524455688,
                "RuleDisabled": false,
                "Description": "mydescription1",
                "TopicPattern": ""
            },
            {
                "RuleName": "rule1",
                "CreatedAt": 1524192248,
                "RuleDisabled": false,
                "Description": "Describe",
                "TopicPattern": "gstasg"
            }
        ],
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

