**Example 1: 已开通完成自动签，撤销链接失败**

已经开通自动签成功，无法撤销

Input: 

```
tccli ess CancelUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小强 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.UserAutoSignEnableAlready",
            "Message": "无法撤销，此用户已开通自动签成功"
        },
        "RequestId": "a97c85196a3e"
    }
}
```

**Example 2: 撤销自动签开通链接成功**

撤销自动签开通链接成功

Input: 

```
tccli ess CancelUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小明 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "RequestId": "a97c85196a3e"
    }
}
```

**Example 3: 未生成自动签链接，撤销链接失败**

还未生成开通自动签链接，无法撤销

Input: 

```
tccli ess CancelUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小红 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.UserAutoSignEnableUrlNotExist",
            "Message": "无法撤销，未生成此用户开通自动签链接"
        },
        "RequestId": "a97c85196a3e"
    }
}
```

