**Example 1: 编辑单条入侵防御封禁列表、放通列表规则（新）**

编辑单条入侵防御封禁列表、放通列表规则（新）

Input: 

```
tccli cfw ModifyBlockIgnoreRuleNew --cli-unfold-argument  \
    --Rule.Comment 放通IP \
    --Rule.DirectionList 1 \
    --Rule.EndTime 2024-11-02 18:44:21 \
    --Rule.Ioc 80.94.95.81 \
    --RuleType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "scc.alert.aiDisposal-GeMvNInoyVWx"
    }
}
```

