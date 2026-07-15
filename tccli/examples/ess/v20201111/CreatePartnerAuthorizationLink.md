**Example 1: 创建应用并且授权子客企业链接**



Input: 

```
tccli ess CreatePartnerAuthorizationLink --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps**v**UEfH3DjwIpMfa0uw \
    --BusinessId jdyxk \
    --PartnerOrganizationId yDxjsUUg*dj*335****4zjEvfko0F1BB \
    --ApplicationInfo.CallbackUrl https://v.qq.com \
    --ApplicationInfo.CallbackKey yDwf3U**kp*8*v********jwIpMfa0uw \
    --ProxyOrganizationInfo.OrganizationOpenId ererer \
    --ProxyOrganizationInfo.OperatorOpenId 2323 \
    --PartnerApplicationId yD3nhUUck***up**U***IGBN50TJsNwY
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1773400421,
        "Link": "https://test.qian.tencent.cn/console/third-app-auth?token=yD3aIUUckpmou8niUxFA3TWyp6dwJwKA",
        "RequestId": "a486dde2-d36a-425f-911b-802e0d36a362"
    }
}
```

**Example 2: 已有授权应用，创建子客企业授权链接**



Input: 

```
tccli ess CreatePartnerAuthorizationLink --cli-unfold-argument  \
    --Operator.UserId yDwf3U*c**s8*v*********wIpMfa0uw \
    --BusinessId jdyxk \
    --PartnerOrganizationId yDxjsUU***j*3***U****jE*fko0F1BB \
    --ApplicationInfo.CallbackUrl https://v.qq.com \
    --ApplicationInfo.CallbackKey yD3nhUUc***eu**p*******N50TJsNwY \
    --ProxyOrganizationInfo.OrganizationOpenId org_open_id \
    --ProxyOrganizationInfo.OperatorOpenId operator_open_id \
    --PartnerApplicationId yD3nhU**kp**********IGBN50TJsNwY
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1773400245,
        "Link": "https://test.qian.tencent.cn/console/third-app-auth?token=yD3aIUUckpmouq0qUxnX3yhReAfE4eqs",
        "RequestId": "cb3df742-c9f7-4938-9574-4e2893d9ee8f"
    }
}
```

