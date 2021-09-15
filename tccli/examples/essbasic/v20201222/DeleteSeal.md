**Example 1: 删除电子印章**



Input: 

```
tccli essbasic DeleteSeal --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb88811f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --UserId 88fb0c591044be771f60aa382cc5ed0e \
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

