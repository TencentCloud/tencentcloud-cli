**Example 1: 编辑放通列表示例**

编辑放通列表示例

Input: 

```
tccli cfw ModifyBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rule.Ioc 100.12.31.2 \
    --Rule.DirectionList 0,1 \
    --Rule.EndTime 2025-01-02 14:39:30 \
    --Rule.Comment test \
    --RuleType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "9a185559-4d5f-40a4-bb56-c5c4a48f86c1"
    }
}
```

