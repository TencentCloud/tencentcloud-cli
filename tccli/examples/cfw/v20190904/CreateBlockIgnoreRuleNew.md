**Example 1: 入侵防御接口新-添加IP为放通列表**

入侵防御接口新-添加IP为放通列表

Input: 

```
tccli cfw CreateBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rules.0.Ioc 11.21.31.41 \
    --Rules.0.DirectionList 0 \
    --Rules.0.EndTime 3000-01-01 00:00:00 \
    --Rules.0.Comment 生产IP放通 \
    --RuleType 2 \
    --CoverDuplicate 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0f493b05-6637-41f5-8977-18a55bdebbff"
    }
}
```

