**Example 1: 修改ACL规则**



Input: 

```
tccli ga2 ModifyGlobalAcceleratorAclRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --GlobalAcceleratorAclPolicyId sp-dz058gbb \
    --GlobalAcceleratorAclRuleId sr-00000msx \
    --Protocol UDP
```

Output: 
```
{
    "Response": {
        "RequestId": "870fbbc5-5820-4bff-a5b5-ae0885e284b0",
        "TaskId": "261f2719-20a4-45e4-84e2-d394018fd672"
    }
}
```

