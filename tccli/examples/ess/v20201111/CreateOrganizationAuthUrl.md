**Example 1: 创建企业认证链接**

创建企业认证链接

Input: 

```
tccli ess CreateOrganizationAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDwfsUUckpsqt647UE6uSrk1ZWhYH56z \
    --Endpoint PC \
    --AuthorizationTypes 1 2 3 \
    --LegalName 11 \
    --UniformSocialCreditCode 11 \
    --OrganizationName 测试企业123123 \
    --AutoJumpUrl https://xxxx.com.cn/xxx
```

Output: 
```
{
    "Response": {
        "AuthUrl": "https://test.qian.tencent.cn/console/register-callback?token=yDwFJUUckpsxxxxxWaLrSa3zzlXQh",
        "ExpiredTime": 1668010213,
        "RequestId": "s168499xxxxx2608083"
    }
}
```

