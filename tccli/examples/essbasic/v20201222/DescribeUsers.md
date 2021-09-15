**Example 1: 查询个人帐号**



Input: 

```
tccli essbasic DescribeUsers --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --UserIds 89dsua9d9sa90dsa****
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Users": [
            {
                "UserId": "同CreateUser生成的UserId",
                "Mobile": "用户手机号(脱敏)",
                "CreatedOn": 1609901339,
                "VerifyStatus": 1,
                "Name": "姓名",
                "VerifiedOn": 1609901339,
                "IdCardType": "ID_CARD",
                "IdCardNumber": "1****************0"
            }
        ]
    }
}
```

