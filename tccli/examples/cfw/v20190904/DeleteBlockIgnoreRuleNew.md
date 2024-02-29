**Example 1: 删除示例**

删除示例

Input: 

```
tccli cfw DeleteBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 100.12.31.2 \
    --Rules.0.RuleType 2 \
    --DeleteAll 0 \
    --RuleType 100
```

Output: 
```
{
    "Response": {
        "RequestId": "19df3039-eec2-4a8a-8a51-d552b9cf67f3"
    }
}
```

