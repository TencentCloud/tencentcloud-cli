**Example 1: 创建个人帐号**



Input: 

```
tccli essbasic CreateUserAndSeal --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --OpenId 88fb0c591044be771f60aa382cc5**** \
    --Mobile 1780095**** \
    --Email test@****.com \
    --Name TestName \
    --IdCardType ID_CARD \
    --IdCardNumber 16259019870907**** \
    --SourceIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "s1611196820113234005",
        "UserId": "abcdef1234567890abcdef1234567890",
        "SealId": "dddscf1234567890abcdef1234567890"
    }
}
```

