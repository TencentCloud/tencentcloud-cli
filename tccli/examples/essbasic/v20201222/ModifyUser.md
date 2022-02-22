**Example 1: 修改个人帐号信息**



Input: 

```
tccli essbasic ModifyUser --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --OpenId  \
    --UserId abcdef1234567890abcdef1234567890 \
    --Mobile 1810099**** \
    --Email test@***.com \
    --Name testname
```

Output: 
```
{
    "Response": {
        "RequestId": "s1611196820113234005",
        "UserId": "1234567890abcdef1234567890abcdef"
    }
}
```

