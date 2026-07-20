**Example 1: 删除ACL规则**



Input: 

```
tccli ga2 DeleteGlobalAcceleratorAclRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-00000kf6 \
    --GlobalAcceleratorAclPolicyId sp-5lkgry59 \
    --GlobalAcceleratorAclRuleIds sr-00000msx
```

Output: 
```
{
    "Response": {
        "RequestId": "d9febac8-ac1a-4caf-93d8-e15f5d51a2c1",
        "TaskId": "9cd20fe4-0557-430c-95df-b06800da12f9"
    }
}
```

