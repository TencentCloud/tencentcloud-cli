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
                "DestPortRange": "ALL",
                "SourceCidr": "2.2.2.2",
                "AliasName": "test1",
                "RuleId": "sr-bf0yxxpp",
                "PolicyId": "ssavdf",
                "Protocol": "string"
            }
        ],
        "PolicyId": "sp-9scxxhdh"
    }
}
```

