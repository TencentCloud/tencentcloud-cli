**Example 1: 精确删除一个封禁 IP**

使用 DescribeBlockIgnoreList 查询目标 IP，传顶层 Direction=""，并将完全匹配项的 Ioc、RuleType 和完整 DirectionList 写入删除项。

Input: 

```
tccli cfw DeleteBlockIgnoreRuleNew --cli-unfold-argument  \
    --DeleteAll 0 \
    --Rules.0.Ioc 192.0.2.10 \
    --Rules.0.DirectionList 0,1 \
    --Rules.0.RuleType 1 \
    --ShowType blocklist
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 精确删除一个放通 IP**

用户要求删除放通列表中的 IP 时，调用 DescribeBlockIgnoreList，传顶层 Direction="" 和 ShowType=whitelist；将完全匹配项的 Ioc、RuleType 和完整 DirectionList 写入删除项。

Input: 

```
tccli cfw DeleteBlockIgnoreRuleNew --cli-unfold-argument  \
    --DeleteAll 0 \
    --Rules.0.Ioc 192.0.2.123 \
    --Rules.0.DirectionList 0,1 \
    --Rules.0.RuleType 2 \
    --ShowType whitelist
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

