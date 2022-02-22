**Example 1: 修改企业默认印章**



Input: 

```
tccli essbasic ModifyOrganizationDefaultSeal --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb88811f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --SealId 3486379737fd34230a247061088dedbd \
    --SourceIp 8.8.8.8
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609748005444321663"
    }
}
```

