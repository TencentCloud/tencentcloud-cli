**Example 1: 提现请求示例**

用于商户向绑定银行卡账户中提现的场景。

Input: 

```
tccli cpdp ApplyWithdrawal --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubAppId your_sub_app_id \
    --SettleAcctNo encrypted_account_no \
    --SettleAcctName encrypted_account_name \
    --CurrencyType RMB \
    --CurrencyUnit 1 \
    --CurrencyAmt 10000 \
    --TranWebName 银行申请的超网号 \
    --IdType 1 \
    --IdCode encrypted_id_code \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0"
    }
}
```

