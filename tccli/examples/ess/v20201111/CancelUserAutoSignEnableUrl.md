**Example 1: 撤销自动签开通流程**

撤销自动签开通流程

Input: 

```
tccli ess CancelUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.UserId  \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小明 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5f54-xxxxxa97c85196a3e"
    }
}
```

