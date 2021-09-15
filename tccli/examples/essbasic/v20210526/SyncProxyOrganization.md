**Example 1: 同步企业信息**



Input: 

```
tccli essbasic SyncProxyOrganization --cli-unfold-argument  \
    --ProxyOrganizationName 渠道侧合作企业名称 \
    --UniformSocialCreditCode xxxxxxxxxxxxxxxxxxxx \
    --BusinessLicense xxxxxxxxxxxxx \
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

