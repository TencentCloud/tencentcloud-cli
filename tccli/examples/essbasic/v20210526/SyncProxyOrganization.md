**Example 1: 同步企业信息**

同步企业信息

Input: 

```
tccli essbasic SyncProxyOrganization --cli-unfold-argument  \
    --ProxyOrganizationName 典子谦示例企业 \
    --UniformSocialCreditCode BOLIU101304662708A  \
    --BusinessLicense aHR0cHM6Ly9jYXBpLndvYS5jb20vhaWwlM0ZpZCUzRGVzc2Jhc2ljJTI2dGFiJTNEYXBp..图片base64省略 \
    --ProxyLegalName 典子谦 \
    --ProxyLegalIdCardType ID_CARD \
    --ProxyLegalIdCardNumber 620000198802020000 \
    --Agent.ProxyOperator.OpenId n31517 \
    --Agent.ProxyOrganizationOpenId org_zhansan \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi
```

Output: 
```
{
    "Response": {
        "RequestId": "8fb09e62-9642-44c8-992b-ddd6e5086293"
    }
}
```

