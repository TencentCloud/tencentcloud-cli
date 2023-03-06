**Example 1: 查看个人自动签开启状态**

查看个人自动签开启状态

Input: 

```
tccli ess DescribeUserAutoSignStatus --cli-unfold-argument  \
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
        "IsOpen": true,
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

