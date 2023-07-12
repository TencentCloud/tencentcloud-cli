**Example 1: ModifyRule**

常用修改

Input: 

```
tccli teo ModifyRule --cli-unfold-argument  \
    --Status disable \
    --Rules.0.Actions.0.NormalAction.Action RangeOriginPull \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Switch \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values on \
    --Rules.0.Actions.1.CodeAction.Action StatusCodeCache \
    --Rules.0.Actions.1.CodeAction.Parameters.0.Name CacheTime \
    --Rules.0.Actions.1.CodeAction.Parameters.0.StatusCode 200 \
    --Rules.0.Actions.1.CodeAction.Parameters.0.Values 20 \
    --Rules.0.Actions.2.RewriteAction.Action ResponseHeader \
    --Rules.0.Actions.2.RewriteAction.Parameters.0.Action set \
    --Rules.0.Actions.2.RewriteAction.Parameters.0.Name Foo \
    --Rules.0.Actions.2.RewriteAction.Parameters.0.Values Bar \
    --Rules.0.Actions.2.RewriteAction.Parameters.1.Action add \
    --Rules.0.Actions.2.RewriteAction.Parameters.1.Name Hello \
    --Rules.0.Actions.2.RewriteAction.Parameters.1.Values World \
    --Rules.0.Actions.2.RewriteAction.Parameters.2.Action del \
    --Rules.0.Actions.2.RewriteAction.Parameters.2.Name Foo2 \
    --Rules.0.Actions.2.RewriteAction.Parameters.2.Values  \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.Values www.shawndai.cn \
    --RuleName new_rule02 \
    --ZoneId zone-26r78x31ny86 \
    --RuleId rule-djuqmq
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

