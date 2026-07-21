**Example 1: 查看ACL规则**



Input: 

```
tccli ga2 DescribeGlobalAcceleratorAclRules --cli-unfold-argument  \
    --GlobalAcceleratorAclPolicyId sp-dz058gbb
```

Output: 
```
{
    "Response": {
        "GlobalAcceleratorAclRuleSet": [
            {
                "Policy": "ACCEPT",
                "Description": "desc",
                "GlobalAcceleratorAclRuleId": "sr-00000msx",
                "GlobalAcceleratorPolicyId": "sp-dz058gbb",
                "Port": "22",
                "Protocol": "UDP",
                "SourceCidrBlock": "10.0.0.0/16"
            },
            {
                "Policy": "ACCEPT",
                "Description": "",
                "GlobalAcceleratorAclRuleId": "sr-dz058gb9",
                "GlobalAcceleratorPolicyId": "sp-dz058gbb",
                "Port": "21",
                "Protocol": "TCP",
                "SourceCidrBlock": "11.0.0.0/16"
            },
            {
                "Policy": "ACCEPT",
                "Description": "desc",
                "GlobalAcceleratorAclRuleId": "sr-io46vtld",
                "GlobalAcceleratorPolicyId": "sp-dz058gbb",
                "Port": "21",
                "Protocol": "TCP",
                "SourceCidrBlock": "11.0.0.0/16"
            }
        ],
        "RequestId": "9f9b10e7-8036-47b7-a5d6-9a43cb758021",
        "TotalCount": 3
    }
}
```

