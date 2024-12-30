**Example 1: 更新规则**



Input: 

```
tccli tcr ModifyImmutableTagRules --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName private \
    --RuleId 2 \
    --Rule.RepositoryPattern immutable/** \
    --Rule.TagPattern release* \
    --Rule.RuleId 2 \
    --Rule.NsName private \
    --Rule.RepositoryDecoration repoMatches \
    --Rule.TagDecoration matches
```

Output: 
```
{
    "Response": {
        "RequestId": "1b40fa6c-9f54-41c2-93f6-623748232016"
    }
}
```

