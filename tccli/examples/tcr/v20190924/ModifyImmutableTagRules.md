**Example 1: 更新规则**



Input: 

```
tccli tcr ModifyImmutableTagRules --cli-unfold-argument  \
    --NamespaceName kofj \
    --RegistryId tcr-mfoeec7x \
    --Rule.RepositoryDecoration repoMatches \
    --Rule.RepositoryPattern ** \
    --Rule.TagPattern ** \
    --Rule.TagDecoration matches \
    --RuleId 19
```

Output: 
```
{
    "Response": {
        "RequestId": "e60d9467-ceb5-4da3-9956-4a9f2d63d37e"
    }
}
```

