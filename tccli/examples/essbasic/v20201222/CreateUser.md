**Example 1: 创建个人帐号**



Input: 

```
tccli essbasic CreateUser --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --OpenId 89874*** \
    --Mobile 1810099**** \
    --Email test@***.com \
    --Name testname \
    --IdCardType ID_CARD \
    --IdCardNumber 14560919980928****
```

Output: 
```
{
    "Response": {
        "RequestId": "s1611196820113234005",
        "UserId": "abcdef1234567890abcdef1234567890"
    }
}
```

