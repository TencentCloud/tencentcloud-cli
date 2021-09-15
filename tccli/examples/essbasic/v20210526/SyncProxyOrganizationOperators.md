**Example 1: 创建签署账号**



Input: 

```
tccli essbasic SyncProxyOrganizationOperators --cli-unfold-argument  \
    --OperatorType CREATE \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --ProxyOrganizationOperators.0.IdCardNumber 610126198003130000 \
    --ProxyOrganizationOperators.0.Name 张三 \
    --ProxyOrganizationOperators.0.Mobile 18740000000 \
    --ProxyOrganizationOperators.0.IdCardType ID_CARD \
    --ProxyOrganizationOperators.0.Id 00498cc8500be9cxxxxxxx3aff766cac
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609731093733170032"
    }
}
```

