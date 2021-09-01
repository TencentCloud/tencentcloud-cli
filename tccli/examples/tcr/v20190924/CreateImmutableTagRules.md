**Example 1: 新建规则**



Input: 

```
tccli tcr CreateImmutableTagRules --cli-unfold-argument  \
    --NamespaceName kofj \
    --RegistryId tcr-mfoeec7x \
    --Rule.RepositoryDecoration repoMatches \
    --Rule.RepositoryPattern ** \
    --Rule.TagPattern ** \
    --Rule.TagDecoration matches
```

Output: 
```
{
    "Response": {
        "RequestId": "e60d9467-ceb5-4da3-9956-4a9f2d63d37e"
    }
}
```

