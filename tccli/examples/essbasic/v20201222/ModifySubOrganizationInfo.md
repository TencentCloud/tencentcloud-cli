**Example 1: 修改子机构信息**



Input: 

```
tccli essbasic ModifySubOrganizationInfo --cli-unfold-argument  \
    --Caller.OperatorId  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId 3768438f76ea49b43b8c819b13438ae3 \
    --LegalMobile 1324567**** \
    --LegalIdCardNumber 1101011998010*****
```

Output: 
```
{
    "Response": {
        "SubOrganizationId": "3768438f76ea49b43b8c819b13438ae3",
        "RequestId": "s1610021071192729274"
    }
}
```

