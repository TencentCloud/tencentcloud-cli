**Example 1: 同步企业信息**

同步企业信息

Input: 

```
tccli essbasic SyncProxyOrganization --cli-unfold-argument  \
    --ProxyOrganizationName 子客企业名称 \
    --UniformSocialCreditCode code \
    --BusinessLicense l \
    --ProxyLegalName name \
    --Agent.ProxyOperator.OpenId proxy-operator-openid \
    --Agent.ProxyOrganizationOpenId proxy-organization-openid \
    --Agent.AppId test-appid
```

Output: 
```
{
    "Response": {
        "RequestId": "s16221xxx14775648"
    }
}
```

