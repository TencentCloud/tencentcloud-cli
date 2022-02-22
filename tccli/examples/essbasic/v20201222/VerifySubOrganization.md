**Example 1: 子机构已完成实名**



Input: 

```
tccli essbasic VerifySubOrganization --cli-unfold-argument  \
    --Caller.OperatorId dolore \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId 3768438f76ea49b43b8c819b13438ae3
```

Output: 
```
{
    "Response": {
        "RequestId": "s1610021120434576212",
        "SubOrganizationId": "3768438f76ea49b43b8c819b13438ae3"
    }
}
```

