**Example 1: 同步渠道合作企业经办人列表**



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
    --ProxyOrganizationOperators.0.Id 00498cc8500be9cxxxxxxx3aff766cac \
    --ProxyOrganizationOperators.1.IdCardNumber 610126198003130001 \
    --ProxyOrganizationOperators.1.Name 李四 \
    --ProxyOrganizationOperators.1.Mobile 1000000000000 \
    --ProxyOrganizationOperators.1.IdCardType ID_CARD \
    --ProxyOrganizationOperators.1.Id 11498cc8500be9cxxxxxxx3aff766cac
```

Output: 
```
{
    "Response": {
        "FailedList": [
            {
                "Id": "11498cc8500be9cxxxxxxx3aff766cac",
                "Message": "手机号码不合法"
            }
        ],
        "RequestId": "s1631673278484637219",
        "Status": 2
    }
}
```

