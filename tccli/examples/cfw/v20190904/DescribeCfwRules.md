**Example 1: 查询入侵防御封禁列表**

RuleType=intrusion_prevention 时通过 ListType 选择 blocklist、whitelist 或 isolate。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType intrusion_prevention \
    --ListType blocklist \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"intrusion_prevention\",\"list_type\":\"blocklist\",\"total\":1}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 2: 查询入侵防御白名单策略**

查询入侵防御白名单策略，ListType 使用 whitelist。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType intrusion_prevention \
    --ListType whitelist \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"intrusion_prevention\",\"list_type\":\"whitelist\",\"total\":1}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 3: 查询入侵防御隔离列表**

按实例 ID 精确查询入侵防御隔离记录，用于写操作前后核验。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType intrusion_prevention \
    --ListType isolate
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"intrusion_prevention\",\"list_type\":\"isolate\",\"total\":1}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

