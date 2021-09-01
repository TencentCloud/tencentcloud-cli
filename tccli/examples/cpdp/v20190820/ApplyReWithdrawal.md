**Example 1: 重新提现请求**

在提现失败后，重新提现

Input: 

```
tccli cpdp ApplyReWithdrawal --cli-unfold-argument  \
    --BusinessType 1 \
    --MidasSecretId midas分配 \
    --MidasSignature 业务计算 \
    --MidasAppId unibank10001 \
    --Body.WithdrawOrderId 36bc512c22000db108080808080808085e8effc1277aee0d0b7cda47 \
    --Body.Date 2020-04-08 \
    --Body.PayAmt 10 \
    --Body.InSubAppId 288126063310047 \
    --Body.OutSubAppId 288126063310038 \
    --Body.MetaData  \
    --Body.ExtendFieldData  \
    --Body.CurrencyType CNY
```

Output: 
```
{
    "Response": {
        "RequestId": "7c8256aa-1a63-402e-ba14-e0e138135eae",
        "WithdrawOrderId": "johny"
    }
}
```

