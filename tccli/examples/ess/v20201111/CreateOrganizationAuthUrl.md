**Example 1: 创建企业认证链接**

我们传递企业名称和企业的统一信用代码。同时，为了确保信息的准确性和合规性，我们要求在进行企业认证时，企业名称和统一信用代码必须与我们传递的信息完全一致。

Input: 

```
tccli ess CreateOrganizationAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDwfsUUckpsqt647UE6uSrk1ZWhYH56z \
    --Endpoint SHORT_URL \
    --AuthorizationTypes 1 2 3 \
    --UniformSocialCreditCode 9144030071526726XG \
    --OrganizationName 典子谦示例企业 \
    --UniformSocialCreditCodeSame True \
    --OrganizationNameSame True
```

Output: 
```
{
    "Response": {
        "AuthUrl": "https://essurl.cn/24VopUGBZyF",
        "ExpiredTime": 1733388643,
        "RequestId": "a34b6e8e-4a3e-444d-8853-b34f90096254"
    }
}
```

