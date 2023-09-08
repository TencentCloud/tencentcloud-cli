**Example 1: 关闭个人自动签**

关闭个人自动签

Input: 

```
tccli ess DisableUserAutoSign --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 典子谦 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.IdCardNumber 620000198802020000
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5fxxxxxe-a97c85196a3e"
    }
}
```

