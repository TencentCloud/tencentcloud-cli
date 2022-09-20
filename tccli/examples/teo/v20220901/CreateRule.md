**Example 1: CreateRule**



Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --Status disable \
    --Rules.0.Actions.0.NormalAction.Action RangeOriginPull \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Switch \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values on \
    --Rules.0.Actions.1.CodeAction.Action StatusCodeCache \
    --Rules.0.Actions.1.CodeAction.Parameters.0.Name CacheTime \
    --Rules.0.Actions.1.CodeAction.Parameters.0.StatusCode 200 \
    --Rules.0.Actions.1.CodeAction.Parameters.0.Values 20 \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.Values test.vernayang.com \
    --RuleName new_rule01 \
    --ZoneId zone-qbjifysd
```

Output: 
```
{
    "Response": {
        "RequestId": "811d2583-310c-41f4-b5e7-abe4074047d4",
        "RuleId": "rule-djuqmq"
    }
}
```

**Example 2: 参数为 OBJECT 类型的创建**



Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --Status disable \
    --Rules.0.Actions.0.NormalAction.Action CacheKey \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name FullUrlCache \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values off \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Values QueryString \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Name Switch \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Values on \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Name Value \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Values name1 name2 \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Name Action \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Values includeCustom \
    --Rules.0.Actions.0.NormalAction.Parameters.5.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.5.Values IgnoreCase \
    --Rules.0.Actions.0.NormalAction.Parameters.6.Name Switch \
    --Rules.0.Actions.0.NormalAction.Parameters.6.Values on \
    --Rules.0.Actions.0.NormalAction.Parameters.7.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.7.Values Header \
    --Rules.0.Actions.0.NormalAction.Parameters.8.Name Switch \
    --Rules.0.Actions.0.NormalAction.Parameters.8.Values on \
    --Rules.0.Actions.0.NormalAction.Parameters.9.Name Value \
    --Rules.0.Actions.0.NormalAction.Parameters.9.Values Language User-Agent \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target extension \
    --Rules.0.Conditions.0.Conditions.0.Values name1 name2 \
    --RuleName new_rule_type \
    --ZoneId zone-26r78x31ny86
```

Output: 
```
{
    "Response": {
        "RequestId": "811d2583-310c-41f4-b5e7-abe4074047d4",
        "RuleId": "rule-djuqdawq"
    }
}
```

