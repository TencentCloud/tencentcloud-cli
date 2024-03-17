**Example 1: 续期医疗个人自动签许可**

给医疗个人自动签许可续期，续期成功返回追加一年后的有效期。

Input: 

```
tccli essbasic ChannelRenewAutoSignLicense --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --UserInfo.Name 典子谦 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.IdCardNumber 620000198802020000 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN
```

Output: 
```
{
    "Response": {
        "LicenseTo": 1715948179,
        "RequestId": "5beb5fxxxxx-a97c85196a3e"
    }
}
```

