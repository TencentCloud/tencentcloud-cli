**Example 1: 查询企业认证状态**

查询企业认证状态

Input: 

```
tccli ess DescribeOrganizationAuthStatus --cli-unfold-argument  \
    --Operator.UserId xxxxxx \
    --UniformSocialCreditCode  \
    --LegalName  \
    --OrganizationName 测试企业
```

Output: 
```
{
    "Response": {
        "AuthRecords": [
            {
                "AuditStatus": 0,
                "AuthType": 3,
                "OperatorMobile": "132****0000",
                "OperatorName": "典*谦"
            }
        ],
        "AuthStatus": 2,
        "IsVerified": true,
        "RequestId": "s1687254031099376002"
    }
}
```

