**Example 1: 添加访问规则**



Input: 

```
tccli gaap CreateSecurityRules --cli-unfold-argument  \
    --PolicyId 字符串 \
    --RuleList.0.Action 字符串 \
    --RuleList.0.Protocol 字符串 \
    --RuleList.0.DestPortRange 字符串 \
    --RuleList.0.AliasName 字符串 \
    --RuleList.0.SourceCidr 字符串
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

