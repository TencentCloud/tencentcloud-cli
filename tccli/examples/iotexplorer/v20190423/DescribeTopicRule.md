**Example 1: 获取规则信息**



Input: 

```
tccli iotexplorer DescribeTopicRule --cli-unfold-argument  \
    --RuleName test_create
```

Output: 
```
{
    "Response": {
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68",
        "Rule": {
            "RuleName": "test_create",
            "Sql": "SELECT * FROM '$thing/up/+/ProductId/#'",
            "Description": "test",
            "Actions": "[{\"forward\":{\"api\":\"http://127.0.0.1:1088/sub.php\"}}]",
            "RuleDisabled": true
        }
    }
}
```

