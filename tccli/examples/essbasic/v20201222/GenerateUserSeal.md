**Example 1: 生成个人用户电子印章**



Input: 

```
tccli essbasic GenerateUserSeal --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb88811f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --UserId 88fb0c591044be771f60aa382cc5ed0e \
    --SealName TestName \
    --SourceIp 10.8.10.10 \
    --IsDefault False
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609748005444321663",
        "SealId": "627caedfb394e410befc101bf0c161f2"
    }
}
```

