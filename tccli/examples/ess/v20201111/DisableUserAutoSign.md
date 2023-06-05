**Example 1: 关闭个人自动签**

关闭个人自动签

Input: 

```
tccli ess DisableUserAutoSign --cli-unfold-argument  \
    --Operator.UserId abc \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小明 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5fxxxxxe-a97c85196a3e"
    }
}
```

