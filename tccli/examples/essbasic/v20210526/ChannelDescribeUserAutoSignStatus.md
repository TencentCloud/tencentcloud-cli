**Example 1: 查看个人自动签开启状态**

查询个人已开通自动签

Input: 

```
tccli essbasic ChannelDescribeUserAutoSignStatus --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --UserInfo.Name 小明 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "IsOpen": true,
        "LicenseFrom": 1684411624,
        "LicenseTo": 1715947624,
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

