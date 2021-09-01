**Example 1: 列出规则**



Input: 

```
tccli tcr DescribeImmutableTagRules --cli-unfold-argument  \
    --RegistryId tcr-mfoeec7x
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "TagDecoration": "matches",
                "RuleId": 19,
                "Disabled": false,
                "RepositoryDecoration": "repoMatches",
                "RepositoryPattern": "**",
                "TagPattern": "**",
                "NsName": "kofj"
            }
        ],
        "EmptyNs": [
            "library"
        ],
        "Total": 3,
        "RequestId": "17eacd5a-b943-4e39-8a7a-3fb7b171c995"
    }
}
```

