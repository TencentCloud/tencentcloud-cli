**Example 1: 获取安全策略详情**



Input: 

```
tccli gaap DescribeSecurityPolicyDetail --cli-unfold-argument  \
    --PolicyId sp-xxxx
```

Output: 
```
{
    "Response": {
        "Status": "UNBIND",
        "ProxyId": "link-gw4sxx8j",
        "DefaultAction": "ACCEPT",
        "RequestId": "1eea4c85-e088-4512-9c6c-480dff91677e",
        "RuleList": [
            {
                "Action": "DROP",
                "DestPortRange": null,
                "SourceCidr": "2.2.2.2",
                "AliasName": "test1",
                "RuleId": "sr-bf0yxxpp"
            },
            {
                "Action": "ACCEPT",
                "DestPortRange": null,
                "SourceCidr": "1.1.1.1",
                "AliasName": "test2",
                "RuleId": "sr-ivgxkdxz"
            }
        ],
        "PolicyId": "sp-9scxxhdh"
    }
}
```

