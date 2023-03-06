**Example 1: 关闭个人自动签**

关闭个人自动签

Input: 

```
tccli ess DisableUserAutoSign --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小明 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

