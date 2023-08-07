**Example 1: 同步子客企业经办人列表**

同步子客企业经办人列表

Input: 

```
tccli essbasic SyncProxyOrganizationOperators --cli-unfold-argument  \
    --OperatorType CREATE \
    --Agent.ProxyAppId c17bdf9c2a7bd****11f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8****9e3968c0ee248f04 \
    --Agent.AppId 65fb0c5910***0aa382cc5ed0e \
    --ProxyOrganizationOperators.0.IdCardNumber 61012****30000 \
    --ProxyOrganizationOperators.0.Name 张三 \
    --ProxyOrganizationOperators.0.Mobile 187*****000 \
    --ProxyOrganizationOperators.0.IdCardType ID_CARD \
    --ProxyOrganizationOperators.0.Id 00498cc8500be9c*****3aff766cac \
    --ProxyOrganizationOperators.1.IdCardNumber 61012*****03130001 \
    --ProxyOrganizationOperators.1.Name 李四 \
    --ProxyOrganizationOperators.1.Mobile 158*****987 \
    --ProxyOrganizationOperators.1.IdCardType ID_CARD \
    --ProxyOrganizationOperators.1.Id 11498cc8500be9c*****3aff766cac
```

Output: 
```
{
    "Response": {
        "FailedList": [
            {
                "Id": "11498cc8500be9c*****3aff766cac",
                "Message": "手机号码不合法"
            }
        ],
        "RequestId": "s1631673278484637219",
        "Status": 2
    }
}
```

