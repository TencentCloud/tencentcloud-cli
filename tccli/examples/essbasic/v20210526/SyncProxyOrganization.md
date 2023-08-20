**Example 1: 同步企业信息**

同步企业信息

Input: 

```
tccli essbasic SyncProxyOrganization --cli-unfold-argument  \
    --ProxyOrganizationName 子客企业名称 \
    --UniformSocialCreditCode code \
    --BusinessLicense l \
    --ProxyLegalName name \
    --ProxyLegalIdCardType ID_CARD \
    --ProxyLegalIdCardNumber 666666200001011066 \
    --Agent.ProxyOperator.OpenId proxy-operator-openid \
    --Agent.ProxyOrganizationOpenId proxy-organization-openid \
    --Agent.AppId test-appid
```

Output: 
```
{
    "Response": {
        "RequestId": "s16221***14775648"
    }
}
```

