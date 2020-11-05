**Example 1: Adding an Access Rule**



Input: 

```
tccli gaap CreateSecurityRules --cli-unfold-argument  \
    --PolicyId String\
    --RuleList.0.SourceCidr String\
    --RuleList.0.Action String\
    --RuleList.0.AliasName String\
    --RuleList.0.Protocol String\
    --RuleList.0.DestPortRange String
```

Output: 
```
{
    "Response": {
        "RequestId": "1eea4c85-e088-4512-9c6c-480dff91677e",
        "RuleIdList": [
            "sr-ishgwan1",
            "sr-ishgwan2"
        ]
    }
}
```

