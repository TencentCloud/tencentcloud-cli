**Example 1: 创建ACL规则**



Input: 

```
tccli ga2 CreateGlobalAcceleratorAclRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --GlobalAcceleratorAclPolicyId sp-dz058gbb \
    --AclEntries.0.Protocol TCP \
    --AclEntries.0.Port 21 \
    --AclEntries.0.SourceCidrBlock 11.0.0.0/16 \
    --AclEntries.0.Policy ACCEPT \
    --AclEntries.0.Description desc
```

Output: 
```
{
    "Response": {
        "RequestId": "d52380f3-5046-43be-8d55-eed0d4250faf",
        "TaskId": "9ea05aea-3301-435d-bc24-4c056ab297ed",
        "GlobalAcceleratorAclRuleIds": [
            "sr-n28npbjx"
        ]
    }
}
```

